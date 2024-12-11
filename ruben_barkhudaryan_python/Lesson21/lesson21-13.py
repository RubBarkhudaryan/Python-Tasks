print("Data Types")
print("Tuple")
print("Exercise 6")

tuple1 = (1, 5, 6, 4, 7, 8, 9, 6, 3, 6, 2, 0)

index = []

for i in range(len(tuple1)):
    if tuple1[i] == 6:
        index.append(i)

print(index)
