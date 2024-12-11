print("Task 1\n")

sum = 0

for i in range(5, 100):
    if i % 5 == 0 or i % 7 == 0:
        sum += i

print("Sum = ", sum)
