print("Data Types")
print("List")
print("Adding new elements to the list - using insert()\n")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

list1.insert(0, ("New first element => ", 0))
print(list1, "\n")

list1.insert(len(list1) // 2, {"Middle Item =>", 4.5})
print(list1, "\n")

list1.insert(len(list1), ["New last element => ", 11])
print(list1, "\n")
