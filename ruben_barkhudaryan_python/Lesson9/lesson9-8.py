print("\nLoops")
print()
print("Nested loops\n")

for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)
        
print()

first = [1, 2, 3]
second = [1, 2, 3]

for i in first:
    for j in second:
        if j == i:
            continue
        print(i, "*", j, " = ", i * j)
