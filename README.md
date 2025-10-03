# 🏫 Student Management System (SMS)

A simple **Student Management System** built in Python using **MySQL**.  
It allows you to **add, update, remove, and display students** along with their marks and calculates totals and averages automatically.

---

## 🚀 Features

- Add new students with marks for multiple subjects  
- Update existing student details and marks  
- Remove students by ID  
- Display all students with their marks, total, and average  
- Checks for duplicate student IDs automatically  

---

## ⚙️ How It Works

1. Connects to a MySQL database using `mysql.connector`  
2. Provides a **menu-driven interface** in the terminal  
3. Uses SQL queries to interact with the `sms_student` table  
4. Calculates **total and average marks** for each student automatically  

---

## 🧩 Requirements

- Python 3.x  
- MySQL database with a table `sms_student`  
- `mysql-connector-python` library  

Install the connector using:  
```bash
pip install mysql-connector-python
