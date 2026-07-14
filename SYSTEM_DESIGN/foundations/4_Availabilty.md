# Availability in System Design

**Status:** Learning
**Created:** 2026-07-08

---

# What is Availability?

Availability is the percentage of time a system remains **operational and accessible** to its users.

In simple words,

> **Availability answers one question: "Can users use the system right now?"**

Even if a system has excellent features, it is useless if users cannot access it.

---

# Why Do We Need Availability?

Imagine you're using:

* UPI to make a payment
* Amazon to place an order
* Netflix to watch a movie

If the server is down,

```text
User

↓

Open App

↓

❌ Server Unavailable
```

the application becomes unusable.

High availability ensures users can continue using the application even when failures occur.

---

# Availability Formula

Availability is usually measured as a percentage.

```
Availability = Uptime / (Uptime + Downtime) × 100
```

Example

Suppose a website runs for

* Uptime = 999 hours
* Downtime = 1 hour

```
Availability

= 999 / (999 + 1)

= 99.9%
```

---

# Understanding "Nines"

| Availability | Downtime per Year (Approx.) |
| ------------ | --------------------------- |
| 99%          | 3.65 Days                   |
| 99.9%        | 8.76 Hours                  |
| 99.99%       | 52 Minutes                  |
| 99.999%      | 5 Minutes                   |

The more "9s" a system has, the less downtime it allows.

---

# Availability vs Reliability

People often confuse these two terms.

They are related but different.

## Availability

Answers

> **Can I access the system?**

Example

A website is always online.

Even if it occasionally returns errors,

it is still considered available.

---

## Reliability

Answers

> **Does the system work correctly without failures?**

Example

A banking application processes every transaction correctly without errors.

---

## Example

Imagine a restaurant.

### High Availability

Restaurant is always open.

But sometimes

* Food is bad.
* Orders are incorrect.

Available ✅

Reliable ❌

---

### High Reliability

Restaurant serves excellent food.

But it opens only three days a week.

Reliable ✅

Available ❌

---

# How is Availability Measured?

Common metrics include

* Uptime
* Downtime
* MTBF (Mean Time Between Failures)
* MTTR (Mean Time To Repair)

---

## MTBF

Measures how long a system runs before failing.

Higher MTBF is better.

---

## MTTR

Measures how quickly the system recovers after a failure.

Lower MTTR is better.

---

# Example

An E-Commerce Website

Requirement

```text
99.99% Availability
```

Possible architecture

```text
               Users

                  │

                  ▼

          Load Balancer

           /     |     \

      Server1 Server2 Server3

             │

             ▼

     Primary Database

             │

     Database Replica
```

If one server fails,

the Load Balancer redirects traffic to the remaining servers.

Users continue using the application.

---

# Techniques to Achieve High Availability

Several architectural techniques improve availability.

---

# 1. Data Replication

Data Replication means maintaining multiple copies of the same data.

```text
Primary Database

      │

      ├────────► Replica 1

      ├────────► Replica 2

      └────────► Replica 3
```

If the primary database fails,

a replica can take over.

---

## Types of Replication

### Synchronous Replication

```text
Client

↓

Primary Database

↓

Replica

↓

Success Response
```

The client receives success only after both databases store the data.

Advantages

* Strong consistency

Disadvantages

* Slower writes

---

### Asynchronous Replication

```text
Client

↓

Primary Database

↓

Success

↓

Replica Later
```

Advantages

* Fast writes

Disadvantages

* Small chance of data loss if the primary crashes before replication.

---

### Semi-Synchronous Replication

A hybrid approach.

The primary waits for at least one replica before acknowledging success.

---

# 2. Redundancy

Redundancy means keeping backup resources ready in case something fails.

Instead of

```text
One Server
```

we keep

```text
Server 1

Server 2

Server 3
```

If one server crashes,

others continue serving users.

Redundancy can exist at multiple levels.

* Server Redundancy
* Database Redundancy
* Network Redundancy
* Storage Redundancy
* Geographic Redundancy
* Cloud Redundancy

---

# 3. Load Balancing

A Load Balancer distributes requests across multiple servers.

```text
Users

↓

Load Balancer

↓

Server1

Server2

Server3
```

Benefits

* Better availability
* Better performance
* Fault tolerance

---

# 4. Failover

Failover means automatically switching to a backup component after a failure.

Example

```text
Primary Server

↓

Failure

↓

Backup Server

↓

Users Continue Working
```

---

## Types of Failover

### Active-Passive

```text
Primary

↓

Handles Traffic


Backup

↓

Waiting
```

When the primary fails,

the backup becomes active.

---

### Active-Active

```text
Load Balancer

↓

Server1

Server2

Server3
```

All servers are active simultaneously.

If one fails,

the others continue serving traffic.

---

# 5. Monitoring and Alerts

Availability cannot be maintained without monitoring.

Common monitoring includes

* CPU Usage
* Memory Usage
* Disk Usage
* Error Rates
* Response Time
* Network Health

Popular tools

* Prometheus
* Grafana
* Datadog
* New Relic

Monitoring systems can automatically alert engineers when issues occur.

---

# Best Practices

* Eliminate Single Points of Failure
* Use Load Balancers
* Replicate Databases
* Deploy Across Multiple Regions
* Monitor Everything
* Automate Failover
* Take Regular Backups
* Use Health Checks

---

# Common Misconceptions

### ❌ Availability means the application never fails.

False.

Failures are expected.

High Availability means the system continues serving users despite failures.

---

### ❌ More servers automatically mean higher availability.

False.

Without load balancing and failover, additional servers provide little benefit.

---

### ❌ Availability and Reliability are the same.

False.

Availability measures accessibility.

Reliability measures correctness.

---

# Advantages

* Better user experience
* Reduced downtime
* Higher customer trust
* Business continuity
* Fault tolerance
* Easier maintenance

---

# Disadvantages

* Higher infrastructure cost
* More operational complexity
* Data synchronization challenges
* More monitoring required

---

# My Questions

## Q1. Are redundant servers always running even if they don't do anything?

**Answer: It depends on the architecture.**

### Active-Passive Architecture

```text
Users

↓

Primary Server ✅

Backup Server 😴 (Idle)
```

The backup server is **running**, but it isn't handling user requests.

It continuously stays synchronized and waits for failures.

If the primary crashes,

```text
Primary ❌

↓

Backup ✅
```

the backup immediately starts serving users.

---

### Active-Active Architecture

```text
Load Balancer

↓

Server1 ✅

Server2 ✅

Server3 ✅
```

Here **all servers are running and handling requests simultaneously**.

No server sits idle.

This architecture is much more common in modern cloud applications like Netflix, Amazon, and Google.

---

## Q2. If one server fails, do the other servers ensure availability?

**Yes, that's exactly the purpose of High Availability.**

Example

Initially

```text
Load Balancer

↓

Server1

Server2

Server3
```

Suppose Server2 crashes.

```text
Load Balancer

↓

Server1

❌ Server2

Server3
```

The Load Balancer detects that Server2 is unhealthy through health checks.

Instead of sending requests there,

it redirects traffic only to healthy servers.

Users often don't even notice the failure.

---

## Q3. What if four servers are already running at 80% capacity, and one server goes down? Can the remaining servers still ensure availability?

**Excellent question. This is a very common real-world problem.**

Let's calculate it.

Initially

```text
4 Servers

Each = 80%

Total Capacity

80 + 80 + 80 + 80

= 320%
```

Suppose one server fails.

Remaining capacity

```text
3 Servers

80 + 80 + 80

= 240%
```

But the incoming traffic still requires **320%**.

The remaining servers now need to handle:

```text
320 / 3 ≈ 107%
```

Each server would need to run at **107%**, which is impossible.

Result:

```text
Server1 → Overloaded

Server2 → Overloaded

Server3 → Overloaded

↓

Slow Responses

↓

Timeouts

↓

Possible Crash
```

So **availability starts degrading**, even though the system is technically still running.

### How do companies solve this?

They **never run production servers close to 100% utilization**.

For example:

```text
4 Servers

Each uses only 50%
```

If one server fails:

```text
Total Load

50 × 4 = 200%

Remaining Servers = 3

Each Handles

200 / 3 ≈ 67%
```

The remaining servers can comfortably absorb the extra load.

Additionally, cloud platforms often use **Auto Scaling**.

```text
4 Servers

↓

One Server Fails

↓

Traffic Redistributed

↓

Auto Scaling Starts New Server

↓

Back to 4 Servers
```

This is why companies keep spare capacity instead of running every server at maximum utilization.

---

# Key Takeaways

* Availability measures whether users can access a system.
* High Availability doesn't mean zero failures—it means users can continue using the system despite failures.
* Redundancy, Load Balancing, Replication, Failover, and Monitoring work together to achieve High Availability.
* Active-Active systems use all servers simultaneously, while Active-Passive systems keep backup servers waiting.
* Production systems intentionally avoid running at full capacity so they can survive server failures.

---

# Summary

```text
                 High Availability

                        │

      ┌─────────────────┼─────────────────┐

      │                 │                 │

      ▼                 ▼                 ▼

 Redundancy      Load Balancer      Replication

      │                 │                 │

      ▼                 ▼                 ▼

 Failover        Healthy Servers     Database Copies

      │

      ▼

 Monitoring & Alerts

      │

      ▼

 Users Can Continue Using The System
```

Availability ensures that users can access a system whenever they need it. High Availability is achieved by designing systems that tolerate failures through redundancy, load balancing, replication, failover mechanisms, and continuous monitoring.
