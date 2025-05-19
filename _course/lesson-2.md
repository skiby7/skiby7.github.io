---
title: Lesson 2 - Python control flow and file execution
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

## Conditional statements

### if-else

Conditional statements allow your program to make decisions and execute different code blocks based on conditions.
In Python the keywords to use boolean values are `True` and `False`.

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition1 is False and condition2 is True
else:
    # code to execute if all above conditions are False
```

When you have an `if-else` statement (like the one above) only the first branch (the codeblocks in a conditional statement are called branches) whose condition is `True` gets executed:

```python
if False:
    # Not executed
elif True:
    # Executed
elif True:
    # Not executed
else:
    # Not executed
```

If you have to check for multiple condition you have to use multiple `if` statements:

```python
if False:
    # Executed
if True:
    # Executed
if True:
    # Executed
```

The condition that can be checked are briefly reported in the table below:

| Operator | Name                     | Example       | Result  |
|----------|--------------------------|---------------|---------|
| `==`     | Equal to                 | `5 == 5`      | `True`  |
| `!=`     | Not equal to             | `3 != 2`      | `True`  |
| `>`      | Greater than             | `10 > 7`      | `True`  |
| `<`      | Less than                | `4 < 6`       | `True`  |
| `>=`     | Greater than or equal to | `8 >= 8`      | `True`  |
| `<=`     | Less than or equal to    | `5 <= 3`      | `False` |
| `is`     | Identity (same object)   | `x is None`   | Depends |
| `is not` | Negated identity         | `x is not []` | `True`  |

Some notes:

- Every condition (e.g. `x >= 10`) can be preceded by the `not` logical operator to negate that condition.
- Conditions can be concatenated using the `and` and `or` logiacal operators (e.g. `x > 10 and x < 20`, `x <= 10 or x >=20`)
- The precedence is `not` > `and` > `or`, so you have to use `()` to group statements together
- The `and` operator returns when he mets the first `False` condition
  ```python
  condition1 = False
  condition2 = True
  if condition1 and condition2:
      pass
  # Condition 2 is not even evaluated!
  ```
- **`==` vs `is`**:
   - `==` checks **value equality**.
   - `is` checks **memory identity** (e.g., `a is b` only if `id(a) == id(b)`).
  ```python

  a = [1, 2, 3]
  b = a          # `b` points to the same object as `a`
  c = [1, 2, 3]  # `c` has the same value but is a different object

  print(a is b)  # True (same object)
  print(a == b)  # True (same value)
  print(a is c)  # False (different objects)
  print(a == c)  # True (same value)
  ```
- **Chaining Comparisons**:
  ```python
  if 1 < x <= 10:  # Equivalent to (1 < x) and (x <= 10)
    print("Valid range")
  ```

### match-case

Since Python version `3.10` and above (knowing on which Pyhton version your code will run is important!) the `match-case` statement has been introduced, providing pattern matching capabilities just like in other languages (which generally use a `switch` statement):

```python
match value:
    case pattern1:
        # code if value matches pattern1
    case pattern2:
        # code if value matches pattern2
    case _:
        # default case (optional)
```

Here's some examples:

```python
# Type matching
value = 3.14
match value:
    case int():
        print("Got an integer")
    case float():
        print("Got a float")  # This will execute
    case str():
        print("Got a string")

# Simple value matching
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not found")  # This will execute
    case 500:
        print("Server error")
    case _:
        print("Unknown status")

# Pattern matching with variables
point = (1, 2)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")  # This will execute
```

## Loops

A `for` loop in Python is a control flow statement that allows you to repeatedly execute a block of code for each item in a sequence (like a list, tuple, string, or other iterable objects). Here's the basic syntax:

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
for i in range(2, 24, 4):
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
for i, v in enumerate(range(2, 24, 4)):
    print(i, v)

# Output:
# 0 2
# 1 6
# 2 10
# 3 14
# 4 18
# 5 22
```

To exit from a for loop you can use the `break` keyword:
```python
for i in range(10):
  if i == 5:
    break
 print(i)
# Output:
# 5
```

The `else` after a for loop is used to run a block of code **if and only if the loop completes normally** (i.e. without a break):
```python
for i in range(10):
  if i == 20:
    break
else:
  # This runs!
  pass

for i in range(10):
  if i == 3:
    break
else:
  # This DOES NOT run!
  pass
```

> ℹ️ **Note:** This concept is a Python feature, do not expect to find it in other languages!

For loops are generally used when you know how many iterations you need beforehand. On the other hand, when you have to run a loop until a condition is met, `while` loops are used:

```python
while condition:
    if something:
        break
else:
    print("Loop finished without breaking")
```

The loop above exits if the `condition` is `True` or `something` is `True`, while the `else` block runs iff `condition` is `True` (just like the `for` loop).

## The `None` value

`None` is a special constant in Python that represents the absence of a value or a `null` value. It is commonly used to indicate that a variable or function doesn't return anything meaningful.
It is falsy in boolean contexts (`if not None` is evaluated as `if True`), but it is not equivalent to `False`, because it explicitly means "no value", so you should explicitly check whether something is `None` or is not `None`:

```python
val = None
if val is None:
  pass
elif val is not None:
  pass

```


## Functions

A function is a reusable block of code that performs a specific task. Functions help in:

- **Modularity**: Breaking code into smaller, manageable parts.
- **Reusability**: Avoid repeating the same code.
- **Abstraction**: Hide complex logic behind a simple interface

```python
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"
```

Let's brake down the code above:

- `def` is the keyword to define a function.
- The name of the function have to follow the `snake_case` naming convention (this is also true for the variables and the file names, but not for classes, more on that later).
- The parameters are defined inside the parentheses and are comma-separated.
- A function can return any type and can have also multiple return values.
- The comment made with a multiline string below the declaration is called `docstring` and, if the text editor supports it, it is shown by the autocompletion system while typing the function name, so that you can have a brief explaination of what the function does.

In Python, functions can have a type hint for both the parameters and the return value (which is `None` by default if nothing is returned)
