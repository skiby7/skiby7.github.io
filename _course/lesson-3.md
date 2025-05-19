---
title: Lesson 3 - Lists, Sets, Tuples and Dictionaries
# date: 2023-05-16 18:00
layout: page
categories: [Programming]
tags: [Python, Programming]
---


In this brief chapeter we will see difference and the syntax to manage lists, sets, tuples and dictionaries, to next move onto more fun stuff.



## Lists

In pyhton lists are a collection of mutable objects, that can be of different types:

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

Another important concept is **slicing**, that allows you to index a portion of a string

What you can do with the lists? Let's see:

- `len(l)`: returns the length of the list
- `l.`
