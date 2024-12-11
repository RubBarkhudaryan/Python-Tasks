print("Data Types")
print("List")
print("Adding new elements to the list - using extend()\n")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

list1.extend([10, 9, 8, 7, 6])
print(list1, "\n")

list1.extend((5, 4, 3, 2, 1))
print(list1, "\n")
