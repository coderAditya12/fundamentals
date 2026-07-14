# Introduction to System Design

**Status:** Completed
**Created:** 2026-07-08

---

# What is System Design?

System Design is the process of designing the architecture, components, databases, APIs, and infrastructure of a software system so that it is **scalable, reliable, maintainable, and efficient**.

It answers questions like:

* How should different components communicate?
* How will millions of users use the application simultaneously?
* Where should data be stored?
* How can failures be handled?
* How can the application remain fast as traffic grows?

Simply put,

> **System Design is the blueprint of a software system before it is built.**

---

# Why is System Design Important?

Imagine building a house.

Before laying bricks, an architect prepares a blueprint showing:

* Number of rooms
* Electrical wiring
* Water supply
* Foundation
* Doors and windows

Without a blueprint, the house may collapse or become difficult to maintain.

Similarly,

before building software, engineers create a system design.

```text
House
    ↓
Blueprint
    ↓
Construction


Software
    ↓
System Design
    ↓
Development
```

---

# Goals of System Design

A good system should be:

* Scalable
* Reliable
* Highly Available
* Maintainable
* Secure
* Fault Tolerant
* Cost Efficient
* Easy to Extend

---

# Why is System Design Important?

## 1. Scalability

A system should continue working even when the number of users increases.

Example

```text
Today

100 Users

↓

One Server


After 2 Years

10 Million Users

↓

Multiple Servers
```

Without scalability,

the application becomes slow or crashes.

---

## 2. Performance

Performance measures how quickly the system responds.

Example

```text
User

↓

Request

↓

Response

50 ms
```

Better performance means

* Lower latency
* Faster response time
* Better user experience

---

## 3. Reliability

Reliability means the application should continue working even if something fails.

Example

If one server crashes,

another server should continue serving users.

```text
Server A ❌

↓

Load Balancer

↓

Server B ✅
```

---

## 4. Maintainability

A system should be easy to modify.

Example

Adding a payment feature should not require rewriting the entire application.

---

## 5. Security

Applications should protect user data.

Examples

* Authentication
* Authorization
* Encryption
* Rate Limiting

---

# High-Level Design (HLD) vs Low-Level Design (LLD)

## High-Level Design (HLD)

HLD focuses on the overall architecture.

Questions answered

* What services are required?
* Which database should be used?
* How will services communicate?
* How many servers are needed?

Example

```text
Client

↓

Load Balancer

↓

API Servers

↓

Database
```

---

## Low-Level Design (LLD)

LLD focuses on implementation details.

Examples

* Class diagrams
* Database schema
* API request/response
* Design patterns
* Algorithms

Example

```text
User

id

name

email

password
```

---

# Scalability

Scalability is the ability of a system to handle increasing traffic.

Two approaches exist.

---

## Vertical Scaling (Scale Up)

Increase the resources of a single server.

```text
Old Server

CPU : 4 Core

RAM : 8 GB


↓

Upgrade


CPU : 32 Core

RAM : 128 GB
```

### Advantages

* Easy to implement
* No application changes

### Disadvantages

* Expensive
* Limited by hardware

---

## Horizontal Scaling (Scale Out)

Instead of making one server bigger,

add more servers.

```text
Before

Client

↓

Server


After

          Load Balancer

          /      |      \

     Server1  Server2  Server3
```

### Advantages

* Better fault tolerance
* Handles millions of users
* Easier to scale

### Disadvantages

* More complex architecture

---

# Load Balancer

A Load Balancer distributes incoming requests among multiple servers.

Without Load Balancer

```text
1000 Users

↓

Server

🔥 Overloaded
```

With Load Balancer

```text
1000 Users

↓

Load Balancer

↓

Server1

Server2

Server3
```

Popular Load Balancers

* Nginx
* HAProxy
* AWS Application Load Balancer
* Cloudflare

---

# Database Design

Databases store application data.

Two major categories.

---

## SQL

Examples

* PostgreSQL
* MySQL
* SQL Server

Characteristics

* Structured data
* ACID transactions
* Relationships
* Joins

---

## NoSQL

Examples

* MongoDB
* Cassandra
* DynamoDB

Characteristics

* Flexible schema
* Horizontal scaling
* High availability

---

# Sharding

As data grows,

one database becomes insufficient.

Instead,

split data across multiple databases.

```text
Users

↓

Shard by User ID

↓

DB 1

DB 2

DB 3
```

---

# Partitioning

Partitioning divides large tables into smaller logical parts.

Example

```text
Orders

↓

2024

2025

2026
```

---

# Caching

Caching stores frequently requested data in fast memory.

Instead of

```text
User

↓

Database

↓

Response
```

we get

```text
User

↓

Redis Cache

↓

Response
```

Database is accessed only if the cache misses.

Popular tools

* Redis
* Memcached

---

# Types of Caching

## Client-side Cache

Stored inside the browser.

Examples

* Local Storage
* Session Storage
* Cookies

---

## Server-side Cache

Stored on the server.

Example

Redis

---

## CDN (Content Delivery Network)

Stores static files close to users.

Example

```text
India User

↓

Indian CDN

↓

Image
```

instead of requesting the image from another continent.

---

# API Communication

Applications communicate using APIs.

---

## REST

Uses HTTP methods.

```text
GET

POST

PUT

DELETE
```

---

## GraphQL

Clients request only the required data.

Example

Instead of

```text
User

Name

Email

Phone

Address
```

Client requests only

```text
User Name
```

---

## gRPC

High-performance communication using Protocol Buffers.

Commonly used in microservices.

---

## WebSockets

Persistent connection for real-time communication.

Examples

* Chat applications
* Live notifications
* Multiplayer games

---

# Message Queues

Sometimes requests should not be processed immediately.

Instead,

they are placed into a queue.

```text
Application

↓

Queue

↓

Worker

↓

Database
```

Popular tools

* Kafka
* RabbitMQ
* AWS SQS

---

# Event-Driven Architecture

Instead of calling services directly,

services publish events.

```text
User Registered

↓

Event

↓

Email Service

Analytics Service

Notification Service
```

---

# Security

Common security mechanisms

* Authentication
* Authorization
* JWT
* OAuth
* OpenID Connect
* HTTPS
* Encryption

---

# Reliability

A reliable system continues working even during failures.

Techniques

* Replication
* Failover
* Backups
* Monitoring
* Health Checks

---

# Example: URL Shortener

Requirements

* Generate short URLs
* Redirect quickly
* Handle millions of requests
* Track analytics

Possible architecture

```text
User

↓

Load Balancer

↓

API Servers

↓

Redis Cache

↓

Database

↓

Analytics Queue

↓

Worker
```

Concepts used

* Load Balancer
* Cache
* Database
* Message Queue
* Sharding
* Rate Limiting

---

# Common Misconceptions

### ❌ System Design is only for FAANG interviews.

False.

Every production application requires system design.

---

### ❌ System Design is only about architecture diagrams.

False.

It includes scalability, networking, databases, caching, security, monitoring, and much more.

---

### ❌ Bigger servers always solve scaling problems.

False.

Horizontal scaling is usually preferred for large systems.

---

# What If Questions

* What happens if one server crashes?
* What happens if the database becomes slow?
* What happens if Redis goes down?
* Why not store everything in cache?
* Why use Kafka instead of direct API calls?
* How does Netflix handle millions of users?

---

# Things You Should Also Know

* CAP Theorem
* Consistent Hashing
* CDN
* Reverse Proxy
* Load Balancing Algorithms
* Replication
* Database Indexing
* Database Sharding
* Message Brokers
* Event Sourcing
* CQRS
* Microservices
* Monolith Architecture

---

# Interview Questions

1. What is System Design?
2. Why is System Design important?
3. Difference between HLD and LLD?
4. Difference between Vertical and Horizontal Scaling?
5. What is Load Balancing?
6. SQL vs NoSQL?
7. What is Caching?
8. What is Sharding?
9. What is a CDN?
10. What is a Message Queue?

---

# Summary

```text
                   System Design

                          │

 ┌──────────────┬──────────────┬──────────────┐
 │              │              │              │
 ▼              ▼              ▼              ▼
Architecture Database     Networking     Security
 │              │              │              │
 ▼              ▼              ▼              ▼
HLD           SQL/NoSQL      APIs        Authentication
LLD           Cache          gRPC        Authorization
Scaling       Sharding       WebSocket   Rate Limiting
```

System Design is the process of designing software systems that are scalable, reliable, secure, and maintainable. It combines architecture, databases, networking, caching, APIs, messaging, and security to build applications capable of handling real-world traffic and failures.
