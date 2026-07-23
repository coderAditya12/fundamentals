# Program vs Process vs Thread

**Status:** Learning
**Created:** 2026-07-08

---

# What is a Program?

A **Program** is a collection of instructions written in a programming language that tells the computer what to do.

It is **not running**.

It is simply stored on disk waiting to be executed.

Think of it as a blueprint or recipe.

Until someone starts following the recipe, nothing happens.

Examples

* Chrome.exe
* VSCode.exe
* python.exe
* node.exe

---

# Why Do We Need Programs?

Programs define the logic of an application.

Without a program, the operating system has nothing to execute.

Example

```text
Calculator.exe

↓

Stored on Disk

↓

Not Running
```

The program contains only instructions.

---

# Program Memory Layout

A program mainly consists of two sections.

```text
Program

│

├── Text Section (Code)

└── Data Section (Global Variables, Constants)
```

---

## Text Section

Contains executable instructions.

Example

```python
print("Hello")
```

This code is stored inside the Text Section.

---

## Data Section

Stores

* Global variables
* Static variables
* Constants

Example

```python
PI = 3.14
```

---

# What is a Process?

A **Process** is a **running instance of a program**.

When you execute a program,

the operating system loads it into memory,

allocates resources,

and starts execution.

At that moment,

the program becomes a process.

---

# Why Do We Need Processes?

Imagine Chrome.

You open Chrome.

Now the operating system must

* Allocate memory
* Allocate CPU time
* Allocate file handles
* Allocate network sockets

The program alone cannot do these things.

The OS creates a **process** to manage all of them.

---

# Program vs Process

```text
Chrome.exe

↓

Double Click

↓

Operating System

↓

Chrome Process
```

---

# Process Memory Layout

Unlike a program,

a process contains much more memory.

```text
+----------------------+
|       Text           |
+----------------------+
|       Data           |
+----------------------+
|       Heap           |
+----------------------+
|       Stack          |
+----------------------+
```

---

## Text

Program instructions.

---

## Data

Global variables.

---

## Heap

Stores dynamically allocated memory.

Example

```python
numbers = []

numbers.append(10)
```

The list object lives in the Heap.

---

## Stack

Stores

* Function calls
* Local variables
* Return addresses

Example

```python
def add(a,b):
    total = a+b
```

Variables

```text
a

b

total
```

are stored inside the Stack.

---

# Process State

A process also contains CPU information.

```text
Process

│

├── Memory

├── CPU Registers

├── Program Counter

├── Open Files

├── Threads

└── Process ID
```

The operating system keeps track of all this information.

---

# What is Context Switching?

Suppose

you have

```text
CPU

↓

Process A
```

After some time,

the operating system pauses it.

```text
CPU

↓

Process B
```

Before switching,

the operating system saves

* CPU Registers
* Program Counter
* Stack Pointer

Later,

Process A resumes exactly where it stopped.

This is called **Context Switching**.

---

# What is a Thread?

A Thread is the **smallest unit of execution** inside a process.

A process can contain one or more threads.

---

# Why Do We Need Threads?

Suppose Chrome has only one thread.

```text
Open Website

↓

Download HTML

↓

Download Images

↓

Download CSS

↓

Render

↓

Handle Mouse Click

↓

Everything Happens One by One
```

The browser would freeze while downloading.

Instead,

Chrome creates multiple threads.

```text
Chrome Process

│

├── UI Thread

├── Render Thread

├── Network Thread

└── JavaScript Thread
```

Now multiple tasks happen simultaneously.

---

# Process vs Thread

```text
Chrome Process

│

├── Thread 1

├── Thread 2

├── Thread 3

└── Thread 4
```

All threads belong to the same process.

---

# Memory Sharing

Processes

```text
Process A

Memory A


Process B

Memory B
```

Processes cannot directly access each other's memory.

---

Threads

```text
Process

│

├── Thread A

├── Thread B

└── Thread C


Shared

Code

Data

Heap
```

Every thread shares

* Code
* Data
* Heap

Each thread has its own

* Stack
* Registers
* Program Counter

---

# Process vs Thread Comparison

| Feature                 | Process    | Thread               |
| ----------------------- | ---------- | -------------------- |
| Smallest Execution Unit | ❌          | ✅                    |
| Own Address Space       | ✅          | ❌                    |
| Shares Memory           | ❌          | ✅                    |
| Creation Cost           | High       | Low                  |
| Context Switch          | Expensive  | Cheaper              |
| Communication           | Slow (IPC) | Fast (Shared Memory) |

---

# Why is Process Creation Expensive?

Creating a process requires the operating system to

* Allocate a new address space
* Allocate page tables
* Create Process Control Block (PCB)
* Allocate kernel resources
* Create at least one thread

```text
New Process

↓

New Memory

↓

New Resources

↓

Ready
```

This takes time.

---

# Why is Thread Creation Cheaper?

A thread already belongs to an existing process.

It simply needs

* New Stack
* Registers
* Program Counter

Everything else is shared.

```text
Existing Process

↓

New Thread

↓

New Stack

↓

Done
```

No new address space is required.

---

# Why is Thread Context Switching Cheaper?

Switching processes

```text
Process A

↓

Save Entire Process State

↓

Switch Address Space

↓

Load Process B
```

Switching threads

```text
Thread A

↓

Save Registers

↓

Load Registers

↓

Continue
```

Since threads share memory,

the operating system doesn't need to switch address spaces.

This makes thread switching faster.

---

# Why Do We Need Both Processes and Threads?

Processes provide

* Isolation
* Security
* Stability

Threads provide

* Concurrency
* Parallelism
* Better resource utilization

Think of it like a company.

```text
Compa
ny

↓

Departments

↓

Employees
```

Company = Process

Employees = Threads

Employees work together because they share the same office.

Different companies cannot freely access each other's offices.

---

# What Happens if a Process Crashes?

Suppose

Chrome has

```text
Chrome Process
```

If the process crashes,

everything inside it stops.

```text
Chrome Process

↓

Crash

↓

All Threads Stop
```

The operating system cleans up

* Memory
* File Handles
* Network Connections

The process disappears.

---

# What Happens if a Thread Crashes?

This depends on the language and operating system.

Usually,

```text
Thread

↓

Crash

↓

Other Threads May Continue
```

However,

in many applications,

a crashing thread can cause the entire process to terminate.

For example, an unhandled exception in the main thread of many applications may bring down the whole process.

How thread failures are handled depends on the runtime (e.g., Java, Python, .NET) and the application's design.

---

# Common Misconceptions

### ❌ Program and Process are the same.

False.

A program is stored on disk.

A process is a running program.

---

### ❌ Every process has only one thread.

False.

Modern applications usually create many threads.

---

### ❌ Threads have their own memory.

False.

Threads share

* Code
* Data
* Heap

Only the Stack is private.

---

### ❌ Processes communicate through shared memory by default.

False.

Processes usually require IPC (Inter-Process Communication).

---

# My Questions

## Q1. Is it possible for a process or thread to crash?

**Yes.**

Both can crash.

* A **process crash** terminates the entire process and all its threads.
* A **thread crash** affects at least that thread. Depending on the runtime and application design, it may or may not terminate the whole process.

---

## Q2. What happens if a process crashes?

The operating system

* Stops execution
* Frees memory
* Closes open files
* Releases network sockets
* Removes the process from the scheduler

All threads inside that process also stop.

---

## Q3. What happens if a thread crashes?

The crashed thread stops executing.

Other threads may continue if the runtime isolates the failure.

In some applications, especially when the main thread crashes or the runtime treats the error as fatal, the entire process exits.

---

## Q4. Why is creating a process more expensive than creating a thread?

Because a process needs its **own independent execution environment**.

The OS must create:

* A new virtual address space
* New page tables
* A Process Control Block (PCB)
* Kernel resources
* The initial thread

A thread only needs:

* A new stack
* CPU registers
* A program counter

Everything else is reused from the existing process.

---

## Q5. Why is thread context switching cheaper than process context switching?

When switching between processes, the OS changes the **entire address space**, updates memory mappings, and restores another process's state.

When switching between threads of the same process, the address space is already shared.

The OS mainly switches:

* Registers
* Stack Pointer
* Program Counter

Since memory mappings stay the same, thread context switching is generally faster.

---

## Q6. Why do we need processes and threads?

A process provides **isolation**.

Imagine Chrome crashes.

Without processes,

the crash could bring down your entire operating system.

Processes isolate applications from each other.

Threads provide **concurrency within a process**.

Instead of doing one task at a time,

Chrome can:

* Download files
* Render the webpage
* Execute JavaScript
* Handle mouse clicks

all at the same time.

In short:

* **Process = Isolation and resource ownership**
* **Thread = Concurrent execution inside a process**

---

# Key Takeaways

* A Program is passive code stored on disk.
* A Process is a running instance of a program.
* A Thread is the smallest unit of execution inside a process.
* Processes have separate memory spaces.
* Threads share memory within the same process.
* Process creation and switching are more expensive than thread creation and switching because processes require separate address spaces and resources.

---

# Summary

```text
                Program
                   │
          (Stored on Disk)
                   │
                   ▼
              Execute
                   │
                   ▼
               Process
                   │
      ┌────────────┼────────────┐
      │            │            │
      ▼            ▼            ▼
  Thread 1     Thread 2     Thread 3
      │            │            │
      └────── Share Code, Data, Heap ──────┘
             (Each has its own Stack)
```

A **Program** is passive code, a **Process** is a running program managed by the operating system, and a **Thread** is the smallest execution unit inside a process. Processes provide isolation and resource management, while threads enable concurrent execution by sharing the process's resources.
