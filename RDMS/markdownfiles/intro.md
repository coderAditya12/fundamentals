
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
database




## How Does a Database Work?
---

## Is the Working of a DBMS the Same as SQL Working?

No.

The working of a Database and SQL are not the same thing.

They are two completely different components that work together to manage data.

To put it simply:

A database is the storage room where data is kept, while SQL is the language you use to communicate with the person managing that storage room.

## My Analogy

Think of it like this:

```text
Database  -> Machine

SQL       -> C Language talking to the machine

ORM/ODM   -> Python built on top of C and other lower level abstractions
```

Examples:

ORMs

* Prisma
* Sequelize
* Hibernate

ODMs

* Mongoose

---

## What People Usually Mean by "How Does a Database Work?"

Most of the time, when someone asks:

> How does a database work?

They are usually asking:

> How does a query get processed?

or

> What is the query execution flow inside a DBMS?

---

## How Does a Database Execute a Query?

Suppose we have the following query.

```sql
SELECT name
FROM users
WHERE age > 18;
```

The DBMS processes this query in multiple stages.

---

## 1. Parsing

The parser checks whether the query is syntactically correct.

Things checked:

* SQL keywords
* Table names
* Column names
* Permissions
* Data types

### Example

Query

```sql
SELECT name
FROM users
WHERE age > 18;
```

Parser checks:

Is `SELECT` valid?

Does table `users` exist?

Does column `name` exist?

Does column `age` exist?

Can this user access the table?

---

### Example of Invalid Query

```sql
SELECT fullname
FROM users;
```

Parser says:

```text
Error:
Column 'fullname' does not exist.
```

Another example

```sql
SELEKT *
FROM users;
```

Parser says

```text
Syntax Error
Unexpected token 'SELEKT'
```

---

## 2. Optimization

After parsing, the query goes to the Query Optimizer.

The optimizer asks:

> What is the fastest way to retrieve this data?

It evaluates multiple execution plans.

Things considered:

* Available indexes
* Table size
* Statistics
* Data distribution
* Join strategies

---

### Example

Suppose there are 10 million users.

Query

```sql
SELECT *
FROM users
WHERE email='abc@gmail.com';
```

### Strategy 1

Scan entire table

```text
Row1
Row2
Row3
...

Row10000000
```

Time: Slow

---

### Strategy 2

Use index

```text
BTree Index


abc@gmail.com
       │
       ▼

Row 5872
```

Time: Fast

Optimizer chooses:

```text
Execution Plan:

Use email_index
```

---

## 3. Execution

After optimization,

The execution engine executes the chosen plan.

Suppose optimizer selected

```text
Use email_index
```

Execution steps

```text
Open Index

↓

Search Key

↓

Find Row Location

↓

Fetch Data

↓

Return Result
```

Result

```text
Name : Aditya

Email : abc@gmail.com
```

---

# Query Processing Pipeline

```text
SQL Query

        │
        ▼

Parser

        │
        ▼

Optimizer

        │
        ▼

Execution Engine

        │
        ▼

Storage Engine

        │
        ▼

Disk / Memory

        │
        ▼

Results Returned
```

---

# SQL Query Execution Order

People often think SQL executes from top to bottom.

But internally, SQL executes differently.

---

## Query Written By Developer

```sql
SELECT department,
       COUNT(*) AS employee_count

FROM employees

WHERE hire_date > '2020-01-01'

GROUP BY department

HAVING COUNT(*) > 5

ORDER BY employee_count DESC;
```

---

## Actual Execution Order

### 1. FROM

Identify source tables.

```text
employees
```

---

### 2. WHERE

Filter rows.

Condition

```sql
hire_date > '2020-01-01'
```

Only matching employees remain.

---

### 3. GROUP BY

Group rows.

Example

```text
Engineering

Engineering

HR

HR

HR
```

Becomes

```text
Engineering

HR
```

---

### 4. HAVING

Filter groups.

Condition

```sql
COUNT(*) > 5
```

Departments having fewer than 5 employees are removed.

---

### 5. SELECT

Select columns.

```sql
department


COUNT(*)
```

Alias created

```sql
employee_count
```

---

### 6. ORDER BY

Sort result.

Descending order.

```text
Engineering 12

Marketing 9

HR 7
```

---

### 7. LIMIT / OFFSET

Restrict returned rows.

Example

```sql
LIMIT 5
```

Return only top 5 rows.

---

# Why Can't We Use SELECT Aliases in WHERE?

Query

```sql
SELECT salary * 12 AS annual_salary

FROM employees

WHERE annual_salary > 100000;
```

This produces an error.

Reason:

SQL execution order.

WHERE executes before SELECT.

At that stage,

`annual_salary` does not exist yet.

---

# Common Misconceptions

### ❌ Database and SQL are the same thing.

Not true.

Database stores data.

SQL communicates with the DBMS.

---

### ❌ Queries execute from top to bottom.

Not true.

They follow the internal execution order discussed above.

---

# What If Questions

* What if no index exists?
* What if two execution plans have the same cost?
* What if statistics are outdated?
* What happens when joins are involved?
* What if the data is already present in memory?
* How does PostgreSQL differ from MySQL in query optimization?

---

# Things You Should Also Know

* B+ Trees
* Clustered Indexes
* Heap Tables
* Query Planner
* Query Cost Estimation
* Storage Engines
* MVCC
* Transactions
* Buffer Pool
* WAL (Write Ahead Logging)
* Checkpoints
* ACID Properties
