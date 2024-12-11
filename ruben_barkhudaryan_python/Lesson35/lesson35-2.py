print("Task 2\n")


def fibonacci(num):
    if num <= 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


sum = 0

for i in range(1, 1000000):
    num = fibonacci(i)
    if num < 1000000:
        sum += num
    else:
        break

print("Sum = ", sum)
