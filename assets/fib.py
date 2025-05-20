def fib_iterative(n: int) -> int:
    if n < 0:
        print("Error!")
        return -1
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        tmp = a
        a = b
        b = tmp + b
    return a

def fib_recursive1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive1(n-1) + fib_recursive1(n-2)


def fib_recursive2(n: int) -> int:
    match n:
        case 0 | 1:
            return n
        case _:
            return fib_recursive2(n-1) + fib_recursive2(n-2)

for i in range(10):
    print(fib_iterative(i))

for i in range(10):
    print(fib_recursive1(i))

for i in range(10):
    print(fib_recursive2(i))
