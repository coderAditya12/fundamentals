# Requirements Analysis

**Status:** Completed
**Created:** 2026-07-08

---

# What is Requirements Analysis?

Requirements Analysis is the process of identifying, understanding, documenting, and validating **what a software system should do** and **how well it should perform** before development begins.

It acts as the foundation of system design because every architectural decision depends on the project requirements.

Simply put,

> **Requirements Analysis answers the question: "What are we building, and what constraints must it satisfy?"**

---

# Why Do We Need Requirements Analysis?

Imagine someone asks you to build an application.

Without gathering requirements, questions immediately arise:

* What features are needed?
* Who will use the application?
* How many users are expected?
* How fast should it be?
* How secure should it be?

If these questions aren't answered first, developers may build the wrong system.

Example

```text
Client

↓

"I need an e-commerce website."

↓

Questions

- Login?
- Payment Gateway?
- Admin Panel?
- Mobile App?
- 1,000 Users?
- 10 Million Users?
```

Requirements Analysis helps answer these questions before development starts.

---

# Types of Requirements

Requirements are mainly divided into two categories.

```text
Requirements

│

├── Functional Requirements

└── Non-Functional Requirements
```

---

# Functional Requirements (FR)

Functional Requirements define **what the system should do**.

They describe the features, functionalities, and business logic of the application.

These requirements directly come from business needs.

---

## Characteristics

* Describe system functionality
* Define business logic
* Specify user interactions
* Define workflows
* Usually visible to end users

---

## Examples

### Authentication

Users should be able to register and log in.

---

### Authorization

Only administrators should be able to delete users.

---

### Data Management

Users should be able to

* Create data
* Read data
* Update data
* Delete data

(CRUD Operations)

---

### Order Management

Customers should be able to

* Place orders
* Cancel orders
* Track orders

---

### Notifications

The system should send an email after an order is successfully placed.

---

## Example

Consider an online shopping website.

Functional requirements could be:

```text
✓ User Registration

✓ Login

✓ Search Products

✓ Add to Cart

✓ Checkout

✓ Payment

✓ Order History
```

Without these features,

the application cannot fulfill its primary purpose.

---

# Non-Functional Requirements (NFR)

Non-Functional Requirements define **how well the system should perform its functions**.

They focus on quality attributes rather than features.

Unlike Functional Requirements,

they usually affect the entire system rather than one specific feature.

---

## Characteristics

* Measure quality
* Affect overall system behavior
* Influence architecture
* Often measurable

---

## Examples

### Performance

The system should respond within **2 seconds** under normal load.

---

### Scalability

The application should support

```text
10,000 Concurrent Users
```

without performance degradation.

---

### Reliability

The application should remain operational even if one server fails.

---

### Availability

The system should maintain

```text
99.9% Uptime
```

---

### Security

* Encrypt passwords
* Encrypt sensitive data
* Use HTTPS
* Protect against SQL Injection
* Protect against XSS

---

### Maintainability

The codebase should

* Follow coding standards
* Be modular
* Be easy to update

---

### Usability

The interface should

* Be easy to understand
* Support accessibility guidelines
* Be responsive on different devices

---

# Functional vs Non-Functional Requirements

| Functional Requirements         | Non-Functional Requirements          |
| ------------------------------- | ------------------------------------ |
| Define **what** the system does | Define **how well** the system works |
| Feature-oriented                | Quality-oriented                     |
| Visible to users                | Usually invisible to users           |
| Based on business requirements  | Based on system quality goals        |
| Examples: Login, Payment        | Examples: Performance, Security      |

---

# Real-World Example

Suppose you're building a **Food Delivery App**.

## Functional Requirements

* User Registration
* Login
* Search Restaurants
* Place Orders
* Online Payment
* Order Tracking
* Reviews and Ratings

These define the application's features.

---

## Non-Functional Requirements

* Response time should be under **2 seconds**
* Support **100,000 concurrent users**
* **99.99% uptime**
* Passwords must be encrypted
* Daily database backups
* API availability should remain above **99.9%**

These define the quality of the application.

---

# How Requirements Influence System Design

Requirements directly affect architectural decisions.

Example

Requirement

```text
Support 10 Million Users
```

Possible Design Decisions

* Load Balancer
* Horizontal Scaling
* Redis Cache
* Database Sharding
* CDN

---

Requirement

```text
Real-Time Chat
```

Possible Design Decisions

* WebSockets
* Message Queue
* Event-Driven Architecture

---

Requirement

```text
High Security
```

Possible Design Decisions

* JWT Authentication
* OAuth
* HTTPS
* Encryption
* Rate Limiting

---

# Functional and Non-Functional Requirements Together

Both types of requirements work together.

Example

```text
Online Banking System

Functional Requirement

↓

Transfer Money


Non-Functional Requirement

↓

Transfer should complete

within 2 seconds

with encrypted communication

and 99.99% availability
```

A feature alone is not enough.

It must also meet performance, security, and reliability expectations.

---

# Common Misconceptions

### ❌ Functional Requirements are more important than Non-Functional Requirements.

False.

Without Non-Functional Requirements, the application may work correctly but still fail under real-world conditions.

Example:

A login feature works correctly but takes **30 seconds** to respond.

Technically, the functionality exists—but the user experience is unacceptable.

---

### ❌ Non-Functional Requirements are optional.

False.

Ignoring scalability, security, or reliability can lead to system failures.

---

### ❌ Performance only means speed.

False.

Performance includes

* Response Time
* Throughput
* Resource Usage
* Latency

---

# Advantages

* Clear project scope
* Better communication between stakeholders
* Reduces misunderstandings
* Guides system architecture
* Helps estimate time and cost
* Improves software quality

---

# Disadvantages

* Gathering requirements can be time-consuming.
* Poorly written requirements lead to incorrect designs.
* Requirements may change during development.
* Missing requirements can be expensive to fix later.

---

# Key Takeaways

* Requirements Analysis is the first step before designing a system.
* Functional Requirements describe **what** the system should do.
* Non-Functional Requirements describe **how well** the system should perform.
* Both types are equally important for building successful software.
* Non-Functional Requirements often drive architectural decisions.

---

# Summary

```text
Requirements Analysis

        │
        ├──────────────────────────────┐
        │                              │
        ▼                              ▼

Functional Requirements      Non-Functional Requirements

        │                              │

   What the system does        How well the system performs

        │                              │

 Login                       Performance

 Payment                     Scalability

 CRUD                        Security

 Notifications               Reliability

 Search                      Availability

 Checkout                    Maintainability
```

Requirements Analysis is the foundation of system design. It ensures that the development team understands both **what features need to be built** and **the quality standards those features must meet**, resulting in systems that are functional, scalable, secure, and reliable.
