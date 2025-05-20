---
title: Lesson 3 - Lists, Sets, Tuples and Dictionaries
# date: 2023-05-16 18:00
layout: page
categories: [Programming]
tags: [Python, Programming]
---


In this brief chapter we will see difference and the syntax to manage lists, sets, tuples and dictionaries, to next move onto more fun stuff.

## Lists

In Python lists are a collection of mutable objects, that can be of different types:

```python
# List constructor
l = list()
# Empty list assignment
l = []
l = [1, 2, 3, "a", "b", "c"]
```

To access an item you can directly index the element you need using its position in the list **starting from 0**:
```python
l[0] # read an item, in this case 1
l[0] = 10 # sets the first element to 10
l[-1] # this references the LAST element -> "c"
l[-2] # -> "b", and so on
l[1000] # you'll get the error IndexError: list index out of range
```

Here's a list of all the main methods and operations available to manipulate lists:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1:3])  # ["banana", "cherry"] (slicing)
fruits[1] = "mango"     # Replace item
fruits.append("orange") # Add to end
fruits.insert(1, "kiwi") # Insert at index
fruits.extend(["grape", "pear"]) # Merge lists
fruits.remove("banana") # Remove by value
popped = fruits.pop(1)  # Remove by index & return
del fruits[0]          # Delete by index
fruits.clear()         # Empty the list
combined = fruits + ["melon", "berry"] # Concatenation
duplicated = [1, 2] * 3               # Repetition ([1, 2, 1, 2, 1, 2])
fruits.sort()                # Alphabetical sort
fruits.reverse()             # Reverse order
count = fruits.count("apple") # Count occurrences
index = fruits.index("cherry") # Find first index
```

An important concept in python is *list comprehension* as it allows you to efficiently create list:

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```

### Copying a list

When you create an object and assign it to a variable, Python stores the object in memory and returns a reference (i.e. the memory address) to that object. You can check this address using the built-in `id()` function.
By default, when you assign an existing variable to a new one, **you are not copying the object itself**, you are copying its reference. This behavior is called **aliasing**.
As a result, if you modify the new variable, the change will also affect the original one, because both variables point to the **same object in memory**.

```python
a = [1, 2, 3]
b = a  # aliasing: b points to the same list as a

b[0] = 99

print(a)  # [99, 2, 3]
print(b)  # [99, 2, 3]
print(id(a) == id(b))  # True
```

Now there are two ways of copying a list:

- **Shallow copy:** Only the top level objects are copied, while nested list are aliased.
- **Deep copy:** Both object and nested lists are copied

Let's see an example of shallow copy:

```python
l = [1, [2, 3]]
r = l[:] # This is the syntax to shallow copy a list
# You can also use the copy method
r = l.copy()

r[0] = 10
r[0][0] = 20
print(l, r)
# l = [1, [20, 3]]
# r = [10, [20, 3]]
```

Here's how to deep copy a list:

```python
import copy

l = [1, [2, 3]]
r = copy.deepcopy(l)

r[0] = 10
r[0][0] = 20
print(l, r)
# l = [1, [2, 3]]
# r = [10, [20, 3]]
```

> ℹ️ **Note:** Shallow copying a list is more efficient as it takes less time and space, but remember that nested objects will be shared between instances.

### List slicing

Slicing allows you to extract a portion of a list using the syntax:

```python
list[start:stop:step]
```
- `start`: Index to begin the slice (inclusive, default = 0).
- `stop`: Index to end the slice (exclusive).
- `step`: Interval between elements (default = 1).

```python
numbers = [0, 1, 2, 3, 4, 5, 6]

numbers[1:5]     # [1, 2, 3, 4]
numbers[:4]      # [0, 1, 2, 3]
numbers[3:]      # [3, 4, 5, 6]
numbers[::2]     # [0, 2, 4, 6]
numbers[::-1]    # [6, 5, 4, 3, 2, 1, 0] (reversed)
```
Notes:

-Negative indices count from the end (-1 is the last item).
- Slicing never raises an error if out of bounds — it just returns what's available.
