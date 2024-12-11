print("Data Types")
print("List")
print("Modifying elements of the list - using []\n")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

list1[0] = 0
print(list1)

list1[:4] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "11.121314151617181920"]
print(list1)

list1[10:] = [11, 12, 13, 14, 15, 16]
print(list1)
