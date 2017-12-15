def fib(n):
    x, y = 0, 1
    while x < n:
        print(x, end=" ")
        x, y = y, x+y
        print()

fib(8000000)
