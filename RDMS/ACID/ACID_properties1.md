# Isolation

## What is Isolation?

Isolation ensures that **multiple transactions running at the same time do not interfere with each other**.

Each transaction should behave as if it is the **only transaction running in the database**, even when many users are accessing the database simultaneously.

---

## Why Do We Need Isolation?

Imagine two users trying to withdraw money from the same bank account at the same time.

Without isolation,

```text
Balance = ₹1000

↓

User A Withdraws ₹700

↓

User B Withdraws ₹500

↓

Final Balance = Incorrect ❌
```

Both users may read the same initial balance, causing incorrect results.

Isolation prevents these concurrency problems.

---

## How Does Isolation Work?

The database controls how concurrent transactions can access data.

```text
Transaction A

        │

        ▼

 Database

        ▲

        │

Transaction B
```

Instead of allowing transactions to modify the same data simultaneously, the database uses locks, snapshots, or versioning depending on the isolation level.

---

# Problems Without Isolation

## Dirty Read

A transaction reads data that **another transaction has modified but has not yet committed**.

If the first transaction later rolls back,

the second transaction has read invalid data.

```text
Transaction A

↓

Balance = ₹500 → ₹1000

(Not Committed)

↓

Transaction B Reads ₹1000

↓

Transaction A Rolls Back

↓

Balance = ₹500
```

Transaction B has read incorrect data.

---

## Non-Repeatable Read

A transaction reads the same row twice but gets different values because another transaction modified and committed the data between the two reads.

```text
Transaction A

↓

Read Balance = ₹1000

↓

Transaction B Updates Balance = ₹1500

↓

Transaction A Reads Again

↓

Balance = ₹1500
```

The same query returned different results.

---

## Phantom Read

A transaction executes the same query twice and receives different numbers of rows because another transaction inserted or deleted matching rows.

```text
Transaction A

↓

SELECT Employees

↓

10 Rows

↓

Transaction B Inserts New Employee

↓

Transaction A Executes Again

↓

11 Rows
```

The extra row is called a **Phantom Row**.

---

# Isolation Levels

Different applications require different balances between **performance** and **data consistency**.

Databases provide four standard isolation levels.

```text
Lowest Consistency
        │
        ▼

Read Uncommitted

↓

Read Committed

↓

Repeatable Read

↓

Serializable

        ▲
Highest Consistency
```

---

## 1. Read Uncommitted

The lowest isolation level.

Transactions can read uncommitted changes made by other transactions.

### Advantages

* Fastest performance

### Disadvantages

* Dirty Reads
* Non-Repeatable Reads
* Phantom Reads

Suitable only when approximate results are acceptable.

---

## 2. Read Committed

A transaction can only read committed data.

Dirty Reads are prevented.

However,

another transaction can still modify data after it has been read.

### Prevents

* Dirty Reads

### Allows

* Non-Repeatable Reads
* Phantom Reads

This is the default isolation level in many databases.

---

## 3. Repeatable Read

Once a transaction reads a row,

it continues seeing the same value throughout the transaction.

### Prevents

* Dirty Reads
* Non-Repeatable Reads

### Allows

* Phantom Reads

Useful for financial calculations where values should not change while processing.

---

## 4. Serializable

The highest isolation level.

Transactions behave as if they are executed **one after another**.

### Prevents

* Dirty Reads
* Non-Repeatable Reads
* Phantom Reads

### Disadvantages

* Slowest performance
* Lower concurrency

Used in systems where correctness is more important than speed, such as banking and healthcare.

---

# Isolation Level Comparison

| Isolation Level  | Dirty Read  | Non-Repeatable Read | Phantom Read |
| ---------------- | ----------- | ------------------- | ------------ |
| Read Uncommitted | ✅ Possible  | ✅ Possible          | ✅ Possible   |
| Read Committed   | ❌ Prevented | ✅ Possible          | ✅ Possible   |
| Repeatable Read  | ❌ Prevented | ❌ Prevented         | ✅ Possible   |
| Serializable     | ❌ Prevented | ❌ Prevented         | ❌ Prevented  |

---

# Durability

## What is Durability?

Durability guarantees that **once a transaction is committed, the data is permanently stored**.

Even if the database crashes, the server loses power, or the operating system restarts, committed data will not be lost.

---

## Why Do We Need Durability?

Imagine a customer successfully transfers money.

```text
Transfer ₹500

↓

Transaction Committed ✅

↓

Server Crash ❌

↓

Money Still Exists ✅
```

If the transaction disappears after the crash,

the database is not durable.

---

## How Does Durability Work?

Before confirming success,

the database writes the transaction safely to persistent storage.

Only then is the transaction marked as committed.

This guarantees that committed transactions can be recovered after failures.

---

# Key Takeaways

* Isolation prevents concurrent transactions from interfering with each other.
* Databases provide four isolation levels with different trade-offs between performance and consistency.
* Dirty Reads, Non-Repeatable Reads, and Phantom Reads are common concurrency problems.
* Durability guarantees that committed transactions survive crashes and failures.
* Higher isolation levels improve correctness but usually reduce performance.
