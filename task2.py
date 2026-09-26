import sqlite3
import time
import hashlib

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    attempts INTEGER DEFAULT 0,
    lock_until REAL DEFAULT 0
)
""")

conn.commit()


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")


# Login user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()

    if user is None:
        print("Invalid username or password.")
        return

    stored_password = user[1]
    attempts = user[2]
    lock_until = user[3]

    # Check lock
    if time.time() < lock_until:
        print("Account is temporarily locked.")
        return

    # Check password
    if hash_password(password) == stored_password:

        cursor.execute(
            "UPDATE users SET attempts = 0 WHERE username = ?",
            (username,)
        )

        conn.commit()

        print("Login successful!")

    else:

        attempts += 1

        if attempts >= 5:

            lock_time = time.time() + 60

            cursor.execute(
                """UPDATE users
                   SET attempts = 0, lock_until = ?
                   WHERE username = ?""",
                (lock_time, username)
            )

            conn.commit()

            print("Too many failed attempts.")
            print("Account locked for 60 seconds.")

        else:

            cursor.execute(
                "UPDATE users SET attempts = ? WHERE username = ?",
                (attempts, username)
            )

            conn.commit()

            print("Wrong password.")
            print("Attempts:", attempts, "/ 5")


# Main program
while True:

    print("\n===== SECURE LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

conn.close()