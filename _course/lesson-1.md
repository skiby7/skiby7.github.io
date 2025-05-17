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

Whenever you see `>>>` it means that the interpreter is expecting an input, while `...` means that you are entering a multiline command (more on that later).

The interpreter follows the *read-eval-print loop* (more about REPL [here](https://en.m.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), so every command issued to the shell will automatically print its output unless it is assigned to a variable:

```text
>>> a = 10
>>> a
10
>>> a + 10
20
```

## Basic math operations

