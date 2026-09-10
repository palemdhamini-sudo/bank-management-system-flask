# Bank Management System – Flask

A simple **Bank Management System REST API** built using **Python Flask, Flask-SQLAlchemy, PostgreSQL, and Docker**.

This project is based on CRUD operations and provides APIs for managing bank accounts, depositing money, withdrawing money, and checking account balances.

## 🚀 Features

* Create a new bank account
* View all bank accounts
* View a specific bank account
* Update bank account details
* Delete a bank account
* Deposit money
* Withdraw money
* Check account balance
* PostgreSQL database integration
* Docker containerization
* REST API-based operations

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **PostgreSQL**
* **Docker**
* **Docker Compose**
* **REST API**

## 📁 Project Structure

```text
bank-management-system-flask/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🗄️ Database

The project uses **PostgreSQL** as the database.

The `bank_accounts` table contains:

| Field          | Description                                |
| -------------- | ------------------------------------------ |
| id             | Unique ID of the account                   |
| account_number | Unique bank account number                 |
| account_holder | Name of the account holder                 |
| account_type   | Type of account such as Savings or Current |
| balance        | Current account balance                    |

## ⚙️ Prerequisites

Make sure the following are installed:

* Python
* Docker Desktop
* Docker Compose
* Visual Studio Code

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bank-management-system-flask.git
```

Move into the project directory:

```bash
cd bank-management-system-flask
```

### 2. Build and start the containers

```bash
docker compose up --build
```

This will start:

* Flask application
* PostgreSQL database

The Flask application runs on:

```text
http://localhost:4000
```

### 3. Test the application

Open another terminal and run:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/test -Method GET
```

Expected response:

```text
message
-------
Bank Management System is working
```

## 🔗 API Endpoints

### 1. Test API

**GET**

```text
/test
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/test -Method GET
```

---

### 2. Create Bank Account

**POST**

```text
/accounts
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts -Method POST -ContentType "application/json" -Body '{"account_number":"10001","account_holder":"Dhamini","account_type":"Savings","balance":5000}'
```

Example response:

```json
{
    "message": "bank account created"
}
```

---

### 3. Get All Accounts

**GET**

```text
/accounts
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts -Method GET
```

Example response:

```json
[
    {
        "id": 1,
        "account_number": "10001",
        "account_holder": "Dhamini",
        "account_type": "Savings",
        "balance": 5000.0
    }
]
```

---

### 4. Get Account by ID

**GET**

```text
/accounts/<id>
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1 -Method GET
```

---

### 5. Update Account

**PUT**

```text
/accounts/<id>
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1 -Method PUT -ContentType "application/json" -Body '{"account_holder":"Dhamini Updated","account_type":"Savings"}'
```

---

### 6. Delete Account

**DELETE**

```text
/accounts/<id>
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1 -Method DELETE
```

---

### 7. Deposit Money

**PUT**

```text
/accounts/<id>/deposit
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1/deposit -Method PUT -ContentType "application/json" -Body '{"amount":2000}'
```

Example response:

```json
{
    "message": "money deposited successfully",
    "balance": 7000.0
}
```

---

### 8. Withdraw Money

**PUT**

```text
/accounts/<id>/withdraw
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1/withdraw -Method PUT -ContentType "application/json" -Body '{"amount":1000}'
```

Example response:

```json
{
    "message": "money withdrawn successfully",
    "balance": 6000.0
}
```

The application checks whether the account has sufficient balance before allowing the withdrawal.

---

### 9. Check Balance

**GET**

```text
/accounts/<id>/balance
```

Example:

```powershell
Invoke-RestMethod -Uri http://localhost:4000/accounts/1/balance -Method GET
```

Example response:

```json
{
    "account_number": "10001",
    "account_holder": "Dhamini",
    "balance": 6000.0
}
```

## 📊 API Summary

| Operation        | Method | Endpoint                  |
| ---------------- | ------ | ------------------------- |
| Test             | GET    | `/test`                   |
| Create Account   | POST   | `/accounts`               |
| Get All Accounts | GET    | `/accounts`               |
| Get Account      | GET    | `/accounts/<id>`          |
| Update Account   | PUT    | `/accounts/<id>`          |
| Delete Account   | DELETE | `/accounts/<id>`          |
| Deposit          | PUT    | `/accounts/<id>/deposit`  |
| Withdraw         | PUT    | `/accounts/<id>/withdraw` |
| Check Balance    | GET    | `/accounts/<id>/balance`  |

## 🐳 Docker

The application uses two Docker services:

### Flask Application

```text
flask_app
```

Runs the Flask REST API on port:

```text
4000
```

### PostgreSQL Database

```text
flask_db
```

Runs PostgreSQL on port:

```text
5432
```

Docker Compose is used to connect the Flask application with PostgreSQL.

## 🧪 Example Flow

A basic banking operation can be performed as follows:

```text
Create Account
      ↓
Deposit Money
      ↓
Check Balance
      ↓
Withdraw Money
      ↓
Check Balance
      ↓
Update Account
      ↓
Delete Account
```

For example:

```text
Initial Balance = ₹5,000

Deposit = ₹2,000

Balance = ₹7,000

Withdraw = ₹1,000

Final Balance = ₹6,000
```

## 🎯 Learning Objectives

This project was created to understand and practice:

* Flask application development
* REST API development
* CRUD operations
* SQLAlchemy ORM
* PostgreSQL database integration
* Docker containerization
* Docker Compose
* HTTP methods such as GET, POST, PUT, and DELETE
* JSON request and response handling
* Basic banking operations

## 🔮 Future Improvements

The project can be extended with:

* User authentication and login
* Password hashing
* Transaction history
* Fund transfer between accounts
* Customer management
* Bank employee/admin login
* Interest calculation
* Account statement generation
* Input validation
* API documentation using Swagger
* Frontend interface

## 👩‍💻 Author

**B.Tech – Computer Science and Engineering (AI & ML)**

This project was developed as a learning project to understand **Flask, REST APIs, SQLAlchemy, PostgreSQL, and Docker**.

## 📄 License

This project is created for educational and learning purposes.
