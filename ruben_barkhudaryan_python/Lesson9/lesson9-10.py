print("\nLoops")
print()
print("Nested loops\n")
print()
print("Perfect numbers from 1 to 100")

n = 2

while n <= 100:
    x_sum = 0
    for i in range(1, n):
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print(f"Perfect number is : {n}")
    n += 1
