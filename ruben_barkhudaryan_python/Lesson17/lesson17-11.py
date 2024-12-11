print("Data Types")
print("List")
print("Modifying all elements of the list\n")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(len(list1)):
    square = list1[i] * list1[i]
    list1[i] = square

print(list1)
