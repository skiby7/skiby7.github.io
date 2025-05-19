---
title: Lesson 3 - Python control flow and file execution
layout: page
categories: [Programming]
tags: [Python, Programming]
---

In the first chapter we have seen how to open a python prompt and interact with the interpreter (REPL), now we will see how to write a (bit) more complex program.

To create your first script you can open your favourite text editor (I personally suggest [Zed](https://zed.dev/download)) and create a new file called `main.py` containig:

```python
print("Hello World!")
```

Now, save and close the file, open your terminal and navigate to that file location:
```bash
ls # this shows the content of the directory you are in
cd directory_name # this allows you to move through the directories
```

Once you are in the same directory as the created before:

```bash
python3 main.py
```

This will start the python interpreter, that will process your program executing the instruction top to bottom.

> ℹ️ **Note:** All the concepts introduced from now on will also apply to the command prompt, but I suggest to experiment creating simple programs and execute them.

## Indentation

In Python, indentation is used to define the structure and scope of code blocks, such as loops, functions, conditionals, and classes. Unlike many other programming languages that use braces `{}`, Python relies on consistent indentation to group statements.

> 📓**Exercise:** open the python shell and try to import `braces` from the `__future__` module (this module contains future features of python that will be released in future releases).

Key Rules of Indentation in Python:
- Indentation must be consistent within a block.
- Use either spaces or tabs, but not both (4 spaces per level are recommended).
- Mismatched indentation causes an `IndentationError`.


## For loop

Before introducing these data structures in python, it is important to introduce loops.
A for loop in Python is a control flow statement that allows you to repeatedly execute a block of code for each item in a sequence (like a list, tuple, string, or other iterable objects). Here's the basic syntax:

```python
for item in iterable:
  # Do something
  pass
```

> ℹ️ **Note:** the `pass` keyword is used as a placeholder to make the program syntactically correct whithout doing anything.

Key definitions:
- **Iterable**: An object capable of returning its members one at a time (e.g., lists, strings, tuples, dictionaries, sets, or range objects).
- **Iterator**: An object that represents a stream of data; it returns the data one element at a time.
- **Loop Variable (item)**: The variable that takes on the value of each element in the iterable during each iteration.
- **Loop Body**: The indented block of code that executes for each iteration.

The `range(start, end, step)` function is used to generate a sequence of numbers programmatically. Let's see the input parameters:

- `start`: The number where the range starts.
- `end`: The number where the range ends. Note that the range stops at `end-1`!
- `step`: The increment (or decrement) at each iteration.

Not all the `range` parameters are mandatory (more on function parameters later), so you can define:

- `range(end)`: This will generate numbers from `0` to `end-1`
- `range(start, end)`: This will generate numbers from `start` to `end-1`
- `range(start, end, step)`: This will generate numbers from `0` to `end-1` incrementing by `step`

Here's an example:
```python
for i in range(2, 24, 4):  # 0 to 4
    print(i)

# Output:
# 2
# 6
# 10
# 14
# 18
# 22
```

Another useful function is `enumerate(iterable)` that allows you to iterate over an object (in the next chapter we will see the main iterable data structures available in python) keeping track of both the index of the iteration and the value:

```python
for i, v in enumerate(range(2, 24, 4)):  # 0 to 4
    print(i, v)

# Output:
# 0 2
# 1 6
# 2 10
# 3 14
# 4 18
# 5 22
```

