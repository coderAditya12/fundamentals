# Just-In-Time (JIT) Compiler

**Status:** Learning
**Created:** 2026-07-08

---

# What is a JIT Compiler?

A **Just-In-Time (JIT) Compiler** is a program that **translates bytecode into machine code while your program is running**.

Instead of interpreting the same instructions again and again, it notices frequently used code, converts it into machine code once, and reuses it.

This makes programs run much faster.

---

# Imagine You're 10 Years Old

Suppose your teacher gives you a book written in **French**, but you only understand **English**.

So you hire a translator.

Every time you read a page:

```text
French Page

↓

Translator

↓

English

↓

You Understand
```

This works...

But what if you read the **same page 1000 times**?

The translator has to translate it **1000 times**.

That is slow.

---

# Interpreter (CPython)

Think of CPython as a translator.

Every single time you ask,

he translates again.

```text
Read Page 1

↓

Translate

↓

Read

↓

Read Page 1 Again

↓

Translate Again

↓

Read

↓

Read Page 1 Again

↓

Translate Again

↓

Read
```

He never remembers his work.

---

# JIT Compiler (PyPy)

Now imagine a smarter translator.

The first time,

he translates the page.

But then he says

> "You're reading this page a lot."

So he writes an English copy.

Now,

instead of translating,

he simply hands you the English version.

```text
French

↓

Translate Once

↓

English Copy

↓

Read Directly

↓

Read Directly

↓

Read Directly
```

Much faster.

---

# Another Analogy

Imagine you travel to school every day.

Without JIT

```text
Home

↓

Ask Google Maps

↓

School

↓

Next Day

↓

Ask Google Maps Again

↓

School

↓

Next Day

↓

Ask Google Maps Again
```

You calculate the route every single day.

---

With JIT

```text
Day 1

↓

Find Best Route

↓

Remember Route

↓

Day 2

↓

Already Know

↓

Day 3

↓

Already Know
```

No more calculations.

---

# How CPython Works

Suppose

```python
for i in range(1000000):
    print(i)
```

CPython executes like this

```text
Bytecode

↓

Interpret

↓

Interpret

↓

Interpret

↓

Interpret

↓

Interpret

↓

Interpret
```

Every loop iteration,

the interpreter keeps reading bytecode.

---

# How PyPy Works

Initially,

PyPy behaves exactly like CPython.

```text
Bytecode

↓

Interpret
```

But after some time,

it notices

> "This loop is running thousands of times."

This frequently executed code is called a **Hot Spot**.

---

# What is a Hot Spot?

A **Hot Spot** is a piece of code that runs repeatedly.

Example

```python
for i in range(10000000):
    total += i
```

The loop body executes **10 million times**.

PyPy thinks

```text
This code is important.

I should optimize it.
```

---

# What Happens Next?

Instead of interpreting the loop forever,

PyPy compiles it into machine code.

```text
Python Code

↓

Bytecode

↓

Interpreter

↓

Hot Spot Found

↓

JIT Compiler

↓

Machine Code

↓

CPU
```

Now,

the CPU executes native instructions directly.

---

# Why is Machine Code Faster?

The CPU understands only machine code.

Without JIT

```text
CPU

↓

Interpreter

↓

Bytecode
```

Every instruction goes through the interpreter.

---

With JIT

```text
CPU

↓

Machine Code
```

No interpreter in the middle.

Fewer steps.

More speed.

---

# Real Example

Suppose you have

```python
def square(x):
    return x * x

for i in range(1000000):
    square(i)
```

CPython

```text
square()

↓

Interpret

↓

Interpret

↓

Interpret

↓

Interpret
```

One million times.

---

PyPy

```text
First Few Calls

↓

Interpret

↓

Hot Spot Detected

↓

Compile square()

↓

Machine Code

↓

Run Machine Code
```

Only the beginning is interpreted.

The rest is native execution.

---

# Does PyPy Compile the Whole Program?

No.

This is a very common misconception.

PyPy compiles **only the frequently executed parts**.

```text
Program

│

├── Rare Function

│      ↓

│   Interpreter

│

├── Hot Loop

│      ↓

│   JIT Compiler

│

└── Another Rare Function

       ↓

   Interpreter
```

Only hot code is optimized.

---

# Why Not Compile Everything?

Compiling takes time.

Imagine compiling every function,

even those called only once.

That would waste time.

Instead,

JIT waits.

If a function becomes important,

then it compiles it.

Hence the name

> **Just-In-Time**

It compiles **just before it's needed**.

---

# CPython vs PyPy

```text
CPython

Bytecode

↓

Interpreter

↓

CPU
```

---

```text
PyPy

Bytecode

↓

Interpreter

↓

Hot Spot?

↓

Yes

↓

JIT Compiler

↓

Machine Code

↓

CPU
```

---

# Advantages

* Much faster for long-running programs.
* Reduces repeated interpretation.
* Optimizes hot code automatically.
* Can approach the speed of compiled languages for some workloads.

---

# Disadvantages

* Extra memory usage.
* Startup is usually slower.
* Short programs may not benefit because the JIT doesn't have enough time to optimize.

---

# Common Misconceptions

### ❌ JIT compiles the whole program.

False.

Only frequently executed code (hot spots) is compiled.

---

### ❌ JIT runs before the program starts.

False.

It works **while the program is running**.

---

### ❌ CPython has a JIT compiler.

Traditional CPython does not use a JIT compiler in the way PyPy does.

---

# What If Questions

* How does PyPy decide when code becomes "hot"?
* Can machine code be discarded later?
* Why doesn't CPython use a JIT by default?
* Why are small programs sometimes slower on PyPy?

---

# Interview Questions

1. What is a JIT compiler?
2. Why is PyPy faster than CPython?
3. What is a hot spot?
4. Why doesn't JIT compile the entire program?
5. What are the advantages and disadvantages of JIT compilation?

---

# Summary

```text
Python Code

        │
        ▼

Bytecode

        │
        ▼

Interpreter

        │
        ▼

Hot Spot Found?

    ┌───────────────┐
    │               │
   No              Yes
    │               │
    ▼               ▼
Keep          JIT Compiler
Interpreting       │
                   ▼
            Machine Code
                   │
                   ▼
                  CPU
```

A JIT compiler improves performance by identifying frequently executed code, compiling it into native machine code during execution, and reusing that machine code instead of interpreting the same bytecode repeatedly. This is why PyPy can be significantly faster than CPython for long-running applications.
