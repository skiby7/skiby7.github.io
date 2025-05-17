---
title: Lesson 1 - Python basics
# date: 2023-05-16 18:00
layout: page
categories: [Programming]
tags: [Python, Programming]
---

First thing first, open a python shell: you can either click on the python icon that appeared after installing it or open a terminal and type `python` or `python3` depending on your installation.
Once opened you will face something like this:

```text
Python 3.13.3 (main, Apr 22 2025, 00:00:00) [GCC 14.2.1 20250110 (Red Hat 14.2.1-7)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Now you can interact with the interpreter issuing commands, declaring variables and so on.
To exit enter the command `exit()` or simply press `CTRL-D` on windows/linux or `CMD-D` on mac.
Whenever you see `>>>` it means that the interpreter is expecting an input, while `...` means that you are entering a multiline command (more on that later).

The interpreter follows the *read-eval-print loop* (more about REPL [here](https://en.m.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), so every command issued to the shell will automatically print its output unless it is assigned to a variable:

```text
>>> a = 10
>>> a
10
>>> a + 10
20
>>>
```

## Basic math operations

Here's a brief table that summarises the math operations in python with their precedence

| Precedence | Operator(s)      | Description                         | Example         |
|------------|------------------|-------------------------------------|-----------------|
| 1 (Highest)| `**`             | Exponentiation                      | `2 ** 3` → 8    |
| 2          | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT      | `-3` → -3       |
| 3          | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo | `10 // 3` → 3 |
| 4          | `+`, `-`         | Addition, subtraction                | `4 + 5` → 9     |
| 5          | `<<`, `>>`       | Bitwise shift operators              | `1 << 2` → 4    |
| 6          | `&`              | Bitwise AND                         | `5 & 3` → 1     |
| 7          | `^`              | Bitwise XOR                         | `5 ^ 3` → 6     |
| 8          | `|`              | Bitwise OR                          | `5 | 3` → 7     |
| 9 (Lowest) | Comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in`, etc.) | Comparison operators | `3 < 5` → True |

> ℹ️ **Note:** Parentheses `()` can be used to override the default precedence.

### A focus on bitwise operations

A computer represents numbers in terms of `1`s and `0`s: bitwise operations act on the binary representation of the operand(s). Let's make some examples:

```text
Bitwise AND
5 & 3 =
1 0 1 (5)
& & &
0 1 1 (3)
-----
0 0 1 (Result = 1)
```

```text
Bitwise OR
1 | 3 =
0 0 1 (1)
| | |
0 1 1 (3)
-----
0 1 1 (Result = 3)
```

```text
Bitwise XOR (eclusive OR)
1 ^ 3 =
0 0 1 (1)
^ ^ ^
0 1 1 (3)
-----
0 1 0 (Result = 2)
```


```text
1 << 2 = 4
0001 -> 0100
8 >> 1 = 4
1000 -> 0100
~2
0010 -> 1101
```

 > **Note:** shifting 1 bit left or right equals respectevely to multiply or divide (much faster than regular operations) the operand by two!

## Basic String Operations

Strings in Python are immutable sequences of Unicode characters. Python provides a rich set of operations for manipulating strings.


```python
s = "Hello"
t = "World"

# Concatenation
combined = s + " " + t  # "Hello World"

# Repetition
echo = s * 3  # "HelloHelloHello"

# Indexing
first_letter = s[0]  # 'H'

# Slicing
part = s[1:4]  # 'ell'

# Length
length = len(s)  # 5

# Membership test
contains = "H" in s  # True
```

To output a string use the `print` function.

> **Note:** in python `#` is a comment, so any character after that will be ignored by the interpreter until the end of the line.

### f-String Formatting

f-Strings in python are a concise and readable way to embed expressions inside string literals using `{}`.

```python
name = "Alice"
age = 30
greeting = f"My name is {name} and I'm {age} years old."
# Output: "My name is Alice and I'm 30 years old."
```

This allow you to easily compose text and print variables in your program.

### Multiline strings

Python supports multiline strings using triple quotes: `'''` or `"""`:

- Multiline strings preserve line breaks and whitespace exactly as written.
- They're commonly used for multiline comments or blocks of formatted text.


```python
text = """This is a
multiline string that spans
several lines."""
print(text)
```

```text
This is a
multiline string that spans
several lines.
```

Multiline strings can be also declared as f-Strings.

### String methods

Strings have also methods (we will see the concept of method when defining classes later on) that allow you to manipulate their value:

```python
s = "Hello"
s.lower()       # 'hello'
s.upper()       # 'HELLO'
s.startswith("He")  # True
s.endswith("o")     # True
s.replace("l", "x") # 'Hexxo'
s.split(" ")        # ['Hello']
" ".join(["A", "B"])  # 'A B'
```

### Escape Characters

[Escape characters](https://en.wikipedia.org/wiki/Escape_character) allow you to include special characters in string literals.

| Escape Sequence | Meaning                |
|-----------------|------------------------|
| `\\`            | Backslash (`\`)        |
| `\'`            | Single quote (`'`)     |
| `\"`            | Double quote (`"`)     |
| `\n`            | New line               |
| `\t`            | Horizontal tab         |
| `\r`            | Carriage return        |
| `\b`            | Backspace              |
| `\f`            | Form feed              |
| `\v`            | Vertical tab           |
| `\a`            | Bell (alert)           |
| `\0`            | Null character         |


