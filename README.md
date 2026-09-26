# Secure Login System with Attack Prevention

## About the Project

The **Secure Login System** is a Python-based authentication project designed to provide a safer way for users to register and log in.

The system protects user passwords using **password hashing** instead of storing them as plain text. It also includes protection against repeated failed login attempts by temporarily locking the account.

## Features

* User registration
* Secure password hashing
* User login authentication
* Failed login attempt tracking
* Temporary account lockout
* Password verification
* Protection against repeated login attempts
* Simple and beginner-friendly implementation

## Technologies Used

* Python
* Password Hashing
* File Handling / Local Storage
* Basic Authentication Concepts

## How It Works

### 1. Registration

The user creates an account by entering a username and password.

### 2. Password Hashing

The password is converted into a secure hash before it is stored.

The original password is not stored directly.

### 3. Login

During login, the entered password is checked against the stored password hash.

### 4. Login Attempt Protection

If a user enters the wrong password multiple times, the system temporarily locks the account.

This helps reduce repeated unauthorized login attempts.

## Example

```text
===== SECURE LOGIN SYSTEM =====

1. Register
2. Login
3. Exit

Enter your choice: 1

Enter username: sneha
Enter password: ********

Registration successful!
```

Login example:

```text
Enter username: sneha
Enter password: ********

Login successful!
Welcome, sneha!
```

After repeated incorrect attempts:

```text
Incorrect password.
Attempts remaining: 2

Incorrect password.
Attempts remaining: 1

Account temporarily locked.
Please try again later.
```

## Security Concepts Learned

This project helps understand basic cybersecurity and authentication concepts such as:

* Authentication
* Password hashing
* Password verification
* Brute-force attack prevention
* Account lockout
* Secure password storage

## Purpose

The main purpose of this project is to learn how secure authentication systems work and understand basic techniques used to protect user accounts from common login-related attacks.

## Future Improvements

* Add a graphical user interface
* Add email verification
* Add password strength checking
* Add database storage
* Add CAPTCHA after multiple failed attempts
* Add multi-factor authentication (MFA)

