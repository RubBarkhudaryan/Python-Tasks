print("\nLoops")
print()
print("Nested loops\n")

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="  ")
    print()

print()

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
