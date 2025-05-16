---
title: Introduction to programming
# date: 2023-05-16 18:00
layout: default
categories: [Programming]
tags: [C, Python, Programming]
---

# Introduction

Programming languages are tools used to write instructions that a computer can understand. Different languages serve different purposes: some are close to the machine (like C), while others are more human-friendly and abstract (like Python).

Not all programming languages are cerated equal: the main differences are static vs dynamic typing and interpreted vs compiled

## Compiled vs interpreted

With compiled languages, the source code is translated once into machine code (binary) by a compiler, creating an executable file with all the needed instructions.

With purely interpreted languages, the code is run line by line by an interpreter that translates the instrunction into machine code.

That are in beetween cases. Some examples are:

- Java that uses a compiler to compile the code into bytecode that is then interpreted.
- Javascript that uses a just-in-time compiler, that translates chunks of code to make the execution faster

An advantage of interpretd languages is that you do not have to compile the code and that usually you have a better error reporting as the interprer knows exactly where the code broke and why.

On the other hand, interpreting line by line the code is an expensive task, so interpreted languages are much slower than the compiled ones, also because the compiler can make as much optimization as he wants during compilation.

## Dynamic vs static typing

A variable in programming is a named container used to store data so you can use and manipulate it later in your code. Variables are also called **lvalues** as they have a location in memory and can appear on the *left* side of an assignemnt, while the **rvalues**are those values or expression that do not have a permanent memory location and are temporary:

```Python
# lvalue = rvalue
x = 10
x = x+10 # here x+10 is an rvalue and, on the right side, x is substituted with its value
3 = x # 3 is an rvalue by definition (it is a constant) and this assignment is not valid
```

 Due to how the computer memory works, programming languages (more precisely compilers and interpreters) have to know how to hanlde a piece of data that can have a variable size, think of 32 vs 64 bits integers/floats or strings, that are `n` bytes long depending on their length. So the type can be set in two ways:

- Statically: you have to declare the type of a variable and you **cannot** change it later

```C
int a = 10; // a is declared as an int
a = "1000"; // it is not possible to assing a string to an int
```
 In some programming languages the type can be inferred by the type of the rvalue:

```go
// This is golang
var a int // Variable declared as int
a = 10 // valid assignment
b := 10.1 // The compiler knows that 10.1 is a float, so b has type float32
```
```C++
// This is C++
auto a = 10; // The compiler assigns the type int to a
```

- Dynamically: you do not have to declare the type of the variable but it is inferred automatically by the rvalue and can change during the program execution (*at runtime*)

```Python
a = 10 # a is an int
a = 10.1 # a is now a float
a = "Hello Nedo!" # is now a string
# From now on a is a string so the instruction below is invalid!
if a > 10:
    # do something

```
 It is easier to write code with dynamic typing, but it is much easier to write bugs with it.


## Variable scoping
