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

 > ℹ️ **Note:** shifting 1 bit left or right equals respectively to multiply or divide (much faster than regular operations) the operand by two!

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

> ℹ️ **Note:** In python `#` is a comment, so any character after that will be ignored by the interpreter until the end of the line.

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

You can also format and style your output using special escape characters:

| Color             | Foreground        | Background        |
|------------------|-------------------|-------------------|
| **Black**         | `\033[30m`        | `\033[40m`        |
| **Red**           | `\033[31m`        | `\033[41m`        |
| **Green**         | `\033[32m`        | `\033[42m`        |
| **Yellow**        | `\033[33m`        | `\033[43m`        |
| **Blue**          | `\033[34m`        | `\033[44m`        |
| **Magenta**       | `\033[35m`        | `\033[45m`        |
| **Cyan**          | `\033[36m`        | `\033[46m`        |
| **White**         | `\033[37m`        | `\033[47m`        |
| **Bright Black**  | `\033[90m`        | `\033[100m`       |
| **Bright Red**    | `\033[91m`        | `\033[101m`       |
| **Bright Green**  | `\033[92m`        | `\033[102m`       |
| **Bright Yellow** | `\033[93m`        | `\033[103m`       |
| **Bright Blue**   | `\033[94m`        | `\033[104m`       |
| **Bright Magenta**| `\033[95m`        | `\033[105m`       |
| **Bright Cyan**   | `\033[96m`        | `\033[106m`       |
| **Bright White**  | `\033[97m`        | `\033[107m`       |

| Effect       | Code         |
|--------------|--------------|
| Reset        | `\033[0m`    |
| Bold         | `\033[1m`    |
| Underline    | `\033[4m`    |
| Reversed     | `\033[7m`    |


> ℹ️ **Note:** After printing a styling escape character you have to print the `reset` character to return to the normal style.

## Basic type conversion

Python supports two types of type conversions: implicit conversion and explicit conversion.

The implicit conversion is automatically performed by Python when it doesn't lose information.

```python
x = 10        # int
y = 2.5       # float
result = x + y  # result is float (12.5)
print(type(result))  # <class 'float'>
```

| Function     | Description                        | Example                | Output           |
|--------------|------------------------------------|------------------------|------------------|
| `int()`      | Converts to integer                | `int("10")`            | `10`             |
| `float()`    | Converts to float                  | `float("3.14")`        | `3.14`           |
| `str()`      | Converts to string                 | `str(123)`             | `"123"`          |
| `bool()`     | Converts to boolean (`True/False`) | `bool(0)`              | `False`          |
| `list()`     | Converts iterable to list          | `list("abc")`          | `['a', 'b', 'c']`|
| `tuple()`    | Converts iterable to tuple         | `tuple([1, 2])`        | `(1, 2)`         |
| `set()`      | Converts iterable to set           | `set([1, 2, 2, 3])`    | `{1, 2, 3}`      |
| `dict()`     | Converts key-value pairs to dict   | `dict([(1, "a")])`     | `{1: 'a'}`       |

> ℹ️ **Note:** We will cover iterable types in [lesson 3](/course/lesson-3/).

```python
a = "5"
b = int(a) + 10
print(b)  # 15
```

