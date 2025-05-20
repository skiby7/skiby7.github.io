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
