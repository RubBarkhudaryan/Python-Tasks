print("Data Types")
print("List")
print("Remove the item with the given index from the list\n")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

removed = list1.pop(3)

print(list1)
print(removed)

removed = list1.pop()

print(list1)
print(removed)
