def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n
time = int(input())
for i in range(time):
    print(fib(i), end = " ")