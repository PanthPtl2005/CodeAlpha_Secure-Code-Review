# Secure Code Review – SQL Injection Demonstration (Flask + SQLite)

## 📌 Project Overview

This project demonstrates a **secure code review** by comparing a **vulnerable** and a **fixed** implementation of a login system in a Flask web application.
The focus is on identifying and mitigating **SQL Injection**, one of the most critical vulnerabilities listed in the **OWASP Top 10**.

The repository contains:

* A vulnerable login implementation using unsafe SQL query construction
* A fixed version using parameterized queries (prepared statements)
* Documentation of the vulnerability and remediation approach

---

## 🧠 Objective

* Understand how SQL Injection vulnerabilities occur
* Analyze insecure coding practices
* Implement secure database interaction techniques
* Apply secure coding principles in real-world scenarios

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Flask
* **Database:** SQLite3

---

## 📂 Project Structure

```
.
├── sqli.py     # SQL Injection vulnerable code
├── sqli-fix.py          # Secure implementation using parameterized queries
├── templates/
│   └── login.html        # Login page
├── example.db            # SQLite database (auto-created)
└── README.md
```

---

## ❌ Vulnerable Implementation

The vulnerable version constructs SQL queries using **string concatenation** with user input.

### Issue

* User input is directly embedded into the SQL query
* Allows attackers to manipulate query logic
* Can result in authentication bypass or data exposure

### Example (Vulnerable)

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

---

## ✅ Fixed Implementation

The fixed version uses **parameterized queries**, separating SQL logic from user input.

### Why It’s Secure

* SQL structure is defined first
* User input is passed as data, not executable SQL
* Prevents SQL Injection completely

### Example (Fixed)

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
c.execute(query, (username, password))
```

---

## 🔐 Vulnerability Mapped

* **OWASP Top 10:** A03 – Injection
* **Type:** SQL Injection
* **Impact:** Unauthorized access, data leakage

---

## 🚀 How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/PanthPtl2005/CodeAlpha_Secure-Code-Review.git
   cd CodeAlpha_Secure-Code-Review
   ```

2. Install dependencies

   ```bash
   pip install flask
   ```

3. Run the application

   For experiencing vulnerable program demonstration run
   ```bash
   python sqli.py
   ```
   For experiencing secure program demonstration run
   ```bash
   python sqli-fix.py
   ```

4. Open in browser

   ```
   http://127.0.0.1:5000
   ```

---

## 📚 Key Learnings

* Never trust user input
* Avoid dynamic SQL query construction
* Always use parameterized queries
* Secure coding is a fundamental part of application security

---

## 🎯 Purpose

This project was completed as part of a **cybersecurity internship task** to demonstrate practical understanding of:

* Secure code review
* Vulnerability identification
* Secure remediation techniques

---

## 🛡️ Disclaimer

This project is for **educational purposes only**.
Do not deploy vulnerable code in production environments.

---

## 📌 Author
Panth Patel


