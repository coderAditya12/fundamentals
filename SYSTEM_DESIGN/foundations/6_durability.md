# Durability in System Design

**Status:** Learning
**Created:** 2026-07-08

---

# What is Durability?

Durability means that **once a system confirms that data has been successfully written, that data should never be lost**, even if failures occur.

In simple words,

> **If the system says "Saved Successfully", the data must remain safe.**

This is one of the most important properties in distributed systems.

---

# Why Do We Need Durability?

Imagine uploading your college project to Google Drive.

```text
Upload File

↓

Success Message

↓

Later...

↓

File Missing ❌
```

Would you trust Google Drive again?

Probably not.

A successful response creates a promise between the system and the user.

Durability ensures that promise is never broken.

---

# Real World Examples

### Dropbox

When you upload a file,

```text
Upload File

↓

Upload Successful

↓

File Permanently Stored
```

If Dropbox loses the file after saying **Upload Successful**,

the system has failed its durability guarantee.

---

### Banking

```text
Transfer ₹10,000

↓

Transaction Successful

↓

Database Crash
```

If the money disappears after the crash,

the banking system is **not durable**.

---

### User Account

Durability isn't limited to files.

Suppose your profile is stored in a database.

```text
Create Account

↓

Success

↓

Database Failure

↓

Account Missing ❌
```

You can no longer log in.

Even though it's "just user data",

durability has been violated.

---

# Durability Depends on the Failure Model

One important thing to understand is that **durability is always defined against specific failures**.

Ask yourself:

> **What failures should my system survive?**

Examples

* A server crashes
* A hard disk fails
* A database node dies
* An entire data center goes down
* An entire cloud region becomes unavailable

Different applications require protection against different failures.

---

# Failure Levels

```text
Failure

│

├── Disk Failure

├── Server Failure

├── Database Failure

├── Data Center Failure

└── Region Failure
```

The stronger your durability guarantee,

the more failures your system can survive.

---

# Recovery Point Objective (RPO)

Before designing durability,

we first decide **how much data loss is acceptable**.

This is called the **Recovery Point Objective (RPO).**

---

## What is RPO?

RPO defines

> **How much data can we afford to lose?**

It is measured in **time**.

---

## Examples

### RPO = 0

```text
Data Loss Allowed

↓

0 Seconds
```

Not even one committed write can be lost.

Suitable for

* Banking
* Payments
* Financial Systems

---

### RPO = 5 Minutes

```text
Data Loss Allowed

↓

Up to 5 Minutes
```

Suitable for

* Analytics
* Logging
* Recommendation Systems

Losing a few minutes of data is acceptable.

---

# Why is RPO Important?

Not every application needs the same durability.

Example

## Payment System

Requirement

```text
RPO = 0
```

Every payment must be preserved.

---

## Analytics System

Requirement

```text
RPO = 10 Minutes
```

Losing a few analytics events is acceptable.

---

Choosing the correct RPO avoids unnecessary cost.

---

# How Do We Achieve Durability?

Durability is achieved using multiple techniques.

```text
Durability

│

├── Persistent Storage

├── Replication

├── Write Quorum

├── Message Queue Persistence

├── Backups

└── Disaster Recovery
```

---

# 1. Persistent Storage

Never store important data only in memory.

Bad

```text
RAM

↓

Power Failure

↓

Data Lost
```

Good

```text
Disk

↓

Power Failure

↓

Data Still Exists
```

---

# 2. Database Replication

One database is not enough.

```text
Primary Database

↓

Replica 1

↓

Replica 2
```

If the primary crashes,

replicas still contain the data.

---

# 3. Synchronous vs Asynchronous Replication

## Synchronous Replication

```text
Client

↓

Primary

↓

Replica

↓

Success Response
```

The client receives success **only after replicas have stored the data**.

### Advantages

* Highest durability
* RPO = 0 (for node failures)

### Disadvantages

* Slower writes

---

## Asynchronous Replication

```text
Client

↓

Primary

↓

Success Response

↓

Replica Later
```

### Advantages

* Faster writes

### Disadvantages

If the primary crashes before replication,

recent data may be lost.

---

# 4. Cross-Region Replication

Suppose your entire cloud region fails.

```text
Region A ❌
```

If all data exists only there,

everything is lost.

Instead,

```text
Region A

↓

Replicate

↓

Region B
```

If Region A fails,

Region B continues serving users.

---

## Why Isn't Cross-Region Replication Always Synchronous?

Imagine

India → USA

Every write must travel thousands of kilometers.

```text
Client

↓

India

↓

USA

↓

Success
```

This increases latency.

Therefore,

many companies use **asynchronous cross-region replication**.

Trade-off

```text
Lower Latency

↓

Small Risk of Data Loss
```

---

# 5. Write Quorum

Suppose we have

```text
3 Database Nodes
```

Instead of writing to only one,

we write to multiple nodes.

Example

```text
Node 1 ✅

Node 2 ✅

Node 3
```

Only after two nodes successfully store the data

does the database return

```text
Success
```

Now,

if one node crashes,

another node already has the data.

---

# Important Note

Many students confuse

```text
R + W > N
```

with durability.

Actually,

that formula is mainly about **consistency**.

Durability focuses on

> **How many copies safely store the data before acknowledging success?**

---

# 6. Durable Message Queues

Suppose your application uses Kafka.

Bad

```text
Producer

↓

Broker

↓

Broker Crash

↓

Message Lost
```

Good

```text
Producer

↓

Broker

↓

Persist to Disk

↓

Replicate

↓

Acknowledge Producer
```

Now the message survives broker failures.

---

# 7. Backups

Replication protects against hardware failures.

Backups protect against

* Human mistakes
* Accidental deletion
* Data corruption
* Ransomware

Example

```text
Database

↓

Daily Backup

↓

Cloud Storage
```

---

# 8. Disaster Recovery

Sometimes an entire region fails.

Example

```text
Earthquake

↓

Data Center Destroyed
```

Without disaster recovery,

the application cannot recover.

With disaster recovery,

another region contains the data.

---

# Common Misconceptions

### ❌ Saving data in RAM is durable.

False.

RAM loses data when power is removed.

---

### ❌ Replication always guarantees zero data loss.

False.

Asynchronous replication can lose recent writes.

---

### ❌ Backups and replication are the same.

False.

Replication improves availability.

Backups protect against accidental deletion and disasters.

---

### ❌ Durability only matters for files.

False.

It applies to every important piece of data.

Examples

* User accounts
* Orders
* Payments
* Messages
* Emails
* Product information

---

# Advantages

* Prevents data loss
* Builds user trust
* Supports disaster recovery
* Protects business-critical information
* Ensures data survives failures

---

# Disadvantages

* Higher storage cost
* Increased write latency (especially synchronous replication)
* More complex architecture
* Additional operational overhead

---

# Key Takeaways

* Durability means **committed data should never be lost**.
* Every application should define its **Recovery Point Objective (RPO)**.
* Different systems require different durability guarantees.
* Replication, Write Quorums, Persistent Storage, Backups, and Disaster Recovery all contribute to durability.
* Synchronous replication provides stronger durability but increases latency.
* Asynchronous replication is faster but may lose recent writes during major failures.

---
## Durability vs Reliability

Durability and Reliability are closely related, but they solve different problems.

A useful way to remember them is:

| Property         | Main Question                                                                |
| ---------------- | ---------------------------------------------------------------------------- |
| **Availability** | Can users access the system?                                                 |
| **Reliability**  | Does the system consistently perform its intended function correctly?        |
| **Durability**   | Once data is acknowledged as saved, will it still exist even after failures? |

### Reliability

Reliability focuses on **correctness**.

It ensures that the system performs its intended operation consistently without failures.

Example:

```text
Transfer ₹1000

↓

Money Deducted

↓

Money Credited

↓

Reliable ✅
```

The transaction completes correctly every time.

---

### Durability

Durability focuses on **data persistence**.

Once the system confirms that data has been saved, that data should never be lost, even if the system crashes immediately afterward.

Example:

```text
Upload File

↓

Upload Successful ✅

↓

Server Crash

↓

File Still Exists ✅
```

If the file disappears after the success message, the system is **not durable**.

---

### Key Difference

Reliability ensures that the system performs operations correctly.

Durability ensures that the **result of those operations is permanently preserved**.

A system can be reliable but not durable.

Example:

```text
Save File

↓

Success Message

↓

Power Failure

↓

File Lost ❌
```

The application correctly processed the request and returned success (reliable behavior), but it failed to preserve the data after the crash (not durable).

---

### Easy Way to Remember

Imagine using Google Photos.

1. **Can you open Google Photos?**

   * Availability

2. **Does it upload the correct photo?**

   * Reliability

3. **Will the photo still be there tomorrow after a server crash?**

   * Durability

---

### Relationship

```text
System Quality

│

├── Availability
│     └── Can users access the system?
│
├── Reliability
│     └── Can the system perform correctly?
│
└── Durability
      └── Can the system preserve acknowledged data?
```

> **Durability is a specific aspect of Reliability that focuses on preserving committed data across failures.** A system may perform operations correctly, but if it loses acknowledged data after a crash, it lacks durability.


# Summary

```text
                    Durability

                         │

      ┌──────────────────┼──────────────────┐

      │                  │                  │

      ▼                  ▼                  ▼

 Persistent        Replication        Write Quorum

 Storage               │                  │

      │                ▼                  ▼

      │        Sync / Async          Multiple Copies

      │

      ▼

 Disaster Recovery

      │

      ▼

 Backups

      │

      ▼

 Data Survives Failures
```

Durability guarantees that once a system acknowledges a successful write, the data remains safe even if failures occur. Achieving durability requires more than just storing data in a database—it involves persistent storage, replication, write quorums, backups, and disaster recovery strategies chosen based on the application's Recovery Point Objective (RPO).

then what is the difference between reliability and durable