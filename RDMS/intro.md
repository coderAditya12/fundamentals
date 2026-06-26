<!-- what is rdbms?
rdbms stand for relational database management system. it is nothing but a software which can interact with our database to get data and store data effectively.

how people used to store data before database?
before database era, people used to store data in different ways like writing, drawing, etc. this was very inefficient and time consuming.they use to store data in books,register, file system and other things.
but these methods were not sufficient. the downside of these system were
1. duplication of data 
2. slow data retrieval
3. not having a structure data like random data
4. there was no relation in data. so data integraity was not maintained.
5. also it was difficult to manage and update data.
6. also it was hard to backup the data.
7.partial update leads to inconsistency
8. no multi user could access it. if they try to access it, it will be locked.
9. also they were vulnerable. because physical books file could be stolen or damaged. -->
# RDBMS

**Status:** Learning
**Created:** 2026-06-26

---

## What is RDBMS?

RDBMS stands for **Relational Database Management System**.

It is a software system that allows us to store, retrieve, update, and manage data efficiently.

It acts as an interface between applications and databases.

Examples:

* MySQL
* PostgreSQL
* Oracle
* SQL Server

---

## How People Used to Store Data Before Databases?

Before databases became popular, people used to store data in different ways such as:

* Writing in books
* Registers
* Physical files
* File systems
* Drawings and documents

These methods worked for small amounts of data but became inefficient as the amount of data increased.

---

## Problems with Traditional Data Storage

### 1. Data Duplication

The same information could be written multiple times.

Example:

```text
Customer name appears in multiple registers.
```

This wastes storage and creates maintenance issues.

---

### 2. Slow Data Retrieval

Finding a specific record required manually searching through books or files.

Example:

```text
Find customer details among 10,000 records.
```

This process is time-consuming.

---

### 3. Lack of Structured Data

Data was often stored in an unorganized manner.

Example:

```text
John
Delhi
25

Apple
500
```

It was difficult to determine relationships between pieces of information.

---

### 4. No Built-in Relationships Between Data

Relationships could exist conceptually, but traditional storage systems had no built-in mechanism to enforce and maintain them automatically.

Example:

```text
Customers
Orders
Payments
```

These were stored separately without links.

As a result, data integrity was difficult to maintain.

---

### 5. Difficult to Manage and Update

Updating information required modifying records manually.

Example:

Changing a customer's address may require updating multiple files.

---

### 6. Backup Was Challenging

Creating backups involved:

* Copying books
* Duplicating files
* Maintaining physical records

This process was expensive and error-prone.

---

### 7. Partial Updates Cause Inconsistency

Suppose a customer's phone number changes.

If some records are updated while others are not, conflicting information exists.

Example:

```text
File A → 9876543210

File B → 9999999999
```

This situation is called **data inconsistency**.

---

### 8. Limited Multi-User Access

Many traditional systems did not support multiple users accessing or modifying records simultaneously.

This could lead to locking issues or conflicting changes.

---

### 9. Vulnerable to Damage or Theft

Physical records can be:

* Lost
* Burned
* Torn
* Stolen
* Damaged by water

This makes data security difficult.

---

## Why Databases Were Introduced

Databases were introduced to solve these problems by providing:

* Structured storage
* Faster retrieval
* Relationships between data
* Backup and recovery mechanisms
* Concurrency control
* Better security
* Reduced redundancy
* Improved consistency

---

## Common Misconceptions

### ❌ Before databases, only physical books were used.

Not entirely true.

People also used file-based systems stored on computers.

Examples:

```text
students.txt
employees.csv
products.xlsx
```

These systems solved some problems but still suffered from redundancy, inconsistency, and poor scalability.

---

## What If Questions

* What if 100 users try to update the same record?
* What if a hard disk crashes?
* What if duplicate customer records are accidentally inserted?
* How does an RDBMS maintain consistency?

---

## Things You Should Also Know

* DBMS vs RDBMS
* ACID Properties
* Primary Keys
* Foreign Keys
* Normalization
* Transactions
* Concurrency Control
* Indexing
