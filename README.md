# SQL Bank Management System

## Overview

The SQL Bank Management System is a command-line banking application developed using Python and MySQL. The project simulates core banking operations such as account creation, user authentication, balance inquiry, cash deposit, withdrawal, fund transfer, and transaction history management.

The application follows a modular architecture where business logic, database operations, and user interactions are separated for better maintainability and scalability.

---

## Features

* User Registration
* Secure User Login
* Account Balance Inquiry
* Cash Deposit
* Cash Withdrawal
* Fund Transfer Between Accounts
* Mini Statement Generation
* Transaction History Tracking
* Automatic Database Table Creation

---

## Technology Stack

### Programming Language

* Python

### Database

* MySQL

### Database Connectivity

* mysql-connector-python

### Development Tools

* VS Code
* Git & GitHub

---

## Database Design

### USERS Table

| Column     | Description                |
| ---------- | -------------------------- |
| ACCOUNT    | Unique Account Number      |
| USERNAME   | Customer Name              |
| EMAIL      | Customer Email             |
| PASSWORD   | User Password              |
| BALANCE    | Current Account Balance    |
| CREATED_AT | Account Creation Timestamp |

### TRANSACTIONS Table

| Column          | Description           |
| --------------- | --------------------- |
| TRANSACTIONID   | Unique Transaction ID |
| ACCOUNT         | Account Number        |
| TRANSACTIONTYPE | CREDIT / DEBIT        |
| AMOUNT          | Transaction Amount    |
| CREATED_AT      | Transaction Timestamp |

---

## Functionalities

### Register User

Creates a new bank account with:

* Username
* Email
* Password
* Initial Deposit Amount

### Login

Validates account number and password before granting access.

### Check Balance

Displays the current available balance.

### Deposit Money

Adds funds to the user's account and records the transaction.

### Withdraw Money

Deducts funds from the user's account after validating sufficient balance.

### Transfer Money

Transfers money from one account to another while maintaining transaction records.

### Mini Statement

Displays recent account transactions including:

* Transaction Type
* Amount
* Date and Time

---

## Project Structure

```text
Bank-Management-System/
│
├── database/
│   ├── connection.py
│   ├── tables.py
│   ├── user_operations.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/SQL-PROJECT-ON-BANK-MANAGEMENT-SYSTEM.git
```

### Navigate to Project Folder

```bash
cd SQL-PROJECT-ON-BANK-MANAGEMENT-SYSTEM
```

### Install Dependencies

```bash
pip install mysql-connector-python
```

### Configure Database

Update MySQL credentials inside:

```python
database/connection.py
```

Example:

```python
host="localhost"
user="root"
password="your_password"
database="bankdb"
```

### Run Application

```bash
python main.py
```

---

## Sample Operations

Welcome to the Small Scale Bank

1. Register
2. Login
```

After Login:

```text
1. Get Balance
2. Withdraw
3. Deposit
4. Transfer
5. Mini Statement
6. Logout
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

* SQL Database Design
* CRUD Operations
* MySQL Integration with Python
* Database Normalization
* Foreign Key Relationships
* Transaction Management
* Backend Application Development
* Modular Programming
* Problem Solving

---

## Future Enhancements

* Password Encryption using Hashing
* OTP-Based Authentication
* Interest Calculation Module
* Loan Management System
* Web-Based Interface using Flask/Django
* Admin Dashboard
* Account Statement Export (PDF/Excel)

---

## Author

**Tanveer Shaik**

* LinkedIn: https://www.linkedin.com/in/sk-tanveer
* GitHub: https://github.com/shaik-tanveer-dev

---

## License

This project is developed for educational and learning purposes.
