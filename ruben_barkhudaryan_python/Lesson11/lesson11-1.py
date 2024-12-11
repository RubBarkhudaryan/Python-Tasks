print("\nRecursion in Python.")

print("\nFactorial with recursion.\n")


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(10):
    fact1 = factorial(i)
    print(f"{i}! = {fact1} \n")


print("\nFibonacci with recursion.\n")


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibonacci((n) - 2) + fibonacci((n) - 1)


n = 10
fib_arr = []
for i in range(n):
    fib_arr.append(fibonacci(i))

print(fib_arr)
