# Python Garbage Collection

**Status:** Learning
**Created:** 2026-07-08

---

# What is Garbage Collection?

Garbage Collection (GC) is Python's mechanism for automatically freeing memory occupied by **unreachable objects**.

It acts as a backup system for **Reference Counting**.

Most objects in Python are destroyed immediately using reference counting.

Garbage Collection exists mainly to clean up **circular references**.

---

# Why Do We Need Garbage Collection?

Suppose we create an object.

```python
numbers = [1, 2, 3]
```

Later,

```python
del numbers
```

Reference count becomes

```text
1 → 0
```

Python immediately destroys the object.

No Garbage Collector is required.

---

# Then Why Does Garbage Collection Exist?

Reference counting has one major limitation.

It **cannot detect circular references**.

Example

```python
class Node:
    pass

node1 = Node()
node2 = Node()

node1.next = node2
node2.next = node1
```

Memory structure

```text
node1
 │
 ▼
+-------+
| Node1 |
+-------+
     │
     ▼
+-------+
| Node2 |
+-------+
     │
     └──────────────┐
                    │
                    ▼
                 Node1
```

Now execute

```python
del node1
del node2
```

Many beginners think

> Both variables are deleted, so memory should be freed.

It is **not**.

---

# Why Doesn't Reference Counting Work Here?

Let's count the references.

Initially

```text
node1

External Reference = 1

Internal Reference = 1

Total = 2
```

Similarly

```text
node2

External Reference = 1

Internal Reference = 1

Total = 2
```

After

```python
del node1
del node2
```

External references disappear.

```text
node1

External = 0

Internal = 1

Total = 1
```

```text
node2

External = 0

Internal = 1

Total = 1
```

Since the reference count never becomes zero,

Reference Counting cannot free the memory.

---

# This is Called a Circular Reference

```text
Object A

↓

Object B

↓

Object A
```

The objects keep each other alive,

even though your program can no longer access them.

---

# How Garbage Collection Solves This

The Garbage Collector periodically searches for unreachable cycles.

It asks

```text
Can this object be reached
from the running program?
```

If

```text
No
```

then

```text
Free Memory
```

---

# Garbage Collection Workflow

```text
Python Program

        │
        ▼

Reference Counting

        │
        ▼

Reference Count = 0 ?

      ┌───────────────┐
      │               │
     Yes              No
      │               │
      ▼               ▼
Destroy Object   Possible Cycle
                      │
                      ▼
             Garbage Collector
                      │
                      ▼
              Detect Cycle
                      │
                      ▼
               Free Memory
```

---

# How Does Python Detect Cycles?

Python maintains a list of container objects.

Examples

* Lists
* Dictionaries
* Class instances
* Sets

Periodically,

the Garbage Collector traverses these objects.

It checks

```text
Can this object still be reached
from the program?
```

If not,

the entire cycle is removed.

---

# Generational Garbage Collection

Python assumes

> Most objects die young.

Because of this,

objects are divided into three generations.

```text
Generation 0

↓

Generation 1

↓

Generation 2
```

---

## Generation 0

Contains newly created objects.

Collected most frequently.

---

## Generation 1

Objects surviving one collection.

Collected less frequently.

---

## Generation 2

Long-lived objects.

Examples

* Imported modules
* Long-running caches
* Global objects

Collected least frequently.

---

# Why Use Generations?

Suppose

```python
for i in range(1_000_000):
    x = [1,2,3]
```

Most objects disappear almost immediately.

Checking every object repeatedly would waste CPU time.

Instead,

Python focuses on Generation 0.

This improves performance significantly.

---

# The gc Module

Python provides the `gc` module to interact with the Garbage Collector.

---

## Manually Trigger Collection

```python
import gc

gc.collect()
```

Forces a garbage collection cycle.

---

## Disable Garbage Collection

```python
import gc

gc.disable()
```

Reference counting still works.

Only cyclic garbage collection is disabled.

---

## Enable Again

```python
gc.enable()
```

---

## Check Whether GC is Enabled

```python
import gc

print(gc.isenabled())
```

---

## Get Collection Thresholds

```python
import gc

print(gc.get_threshold())
```

Example

```text
(700, 10, 10)
```

These values determine when Python triggers garbage collection.

---

# When Should You Disable GC?

Usually,

**Never.**

Only advanced applications

* Game engines
* High-frequency trading
* Scientific simulations

sometimes disable GC during performance-critical sections.

---

# Example

```python
import gc

gc.disable()

# Performance-critical work

gc.enable()
gc.collect()
```

---

# Why Doesn't Python Use Only Garbage Collection?

Imagine

```python
x = [1,2,3]
```

Then

```python
del x
```

Should Python

Scan the entire memory?

That would be expensive.

Instead,

Reference Counting immediately destroys the object.

Only complicated cases require Garbage Collection.

---

# Reference Counting vs Garbage Collection

| Reference Counting   | Garbage Collection          |
| -------------------- | --------------------------- |
| Immediate            | Periodic                    |
| Very Fast            | Slower                      |
| Handles most objects | Handles circular references |
| Counter based        | Graph traversal             |

Both systems work together.

---

# Advantages

* Automatic memory cleanup
* Handles circular references
* Prevents memory leaks
* Reduces manual memory management
* Improves program stability

---

# Limitations

* Periodic scanning consumes CPU
* Can introduce small pauses
* Doesn't immediately run after every cycle
* Cannot fix memory leaks caused by native C extensions

---

# Common Misconceptions

### ❌ Garbage Collection frees every object.

False.

Reference Counting frees most objects.

---

### ❌ `del` immediately destroys an object.

Not always.

It removes one reference.

The object is destroyed only if the reference count becomes zero.

---

### ❌ Garbage Collection runs continuously.

False.

It runs periodically based on thresholds.

---

### ❌ Disabling GC causes memory leaks immediately.

False.

Reference Counting continues to work.

Only circular references remain uncleared.

---

# What If Questions

* What happens if Garbage Collection is disabled?
* What if millions of circular references are created?
* Why doesn't Python use only Garbage Collection?
* Why doesn't Python use only Reference Counting?
* Can circular references occur with lists and dictionaries?

---

# Things You Should Also Know

* Reference Counting
* Memory Allocator
* pymalloc
* Weak References (`weakref`)
* Global Interpreter Lock (GIL)
* Object Graph
* Memory Profiling

---

# Interview Questions

1. What is Garbage Collection?
2. Why does Python need Garbage Collection?
3. What is a circular reference?
4. Why can't Reference Counting remove circular references?
5. What is the `gc` module?
6. What does `gc.collect()` do?
7. What happens if `gc.disable()` is called?
8. Explain Generational Garbage Collection.

---

# My Questions

* How does Python traverse the object graph?
* What algorithm does the cyclic garbage collector use?
* How expensive is `gc.collect()`?
* How do weak references solve circular reference problems?

---

# Summary

```text
Object Created
       │
       ▼
Reference Counting
       │
       ▼
Reference Count = 0 ?
       │
 ┌─────┴─────┐
 │           │
Yes          No
 │           │
 ▼           ▼
Free      Still Alive
               │
               ▼
      Circular Reference?
               │
        ┌──────┴──────┐
        │             │
       No            Yes
        │             │
        ▼             ▼
      Keep      Garbage Collector
                     │
                     ▼
                Detect Cycle
                     │
                     ▼
                 Free Memory
```

Garbage Collection complements Reference Counting by detecting and removing circular references that cannot be freed through reference counting alone. Together, they provide Python with an efficient and automatic memory management system.
