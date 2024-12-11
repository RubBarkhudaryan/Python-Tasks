print("Data Types")
print("List")
print("Checking if all elements of the list are true")

list1 = [9, 5, 4, 2, 11, 8, 1, 7, 6, 3, 10, 12]
list2 = [9, 5, 4, 2, 11, 8, 1, 7, 6, 0, 3, 10, False]
list3 = [0, "", False]
list4 = []


print("If all items are true => ", all(list1))
print("If one item is false => ", all(list2))
print("If all items are false => ", all(list3))
print("If list is empty => ", all(list4))
