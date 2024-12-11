print("Data Types")
print("List")
print("Remove the first occurence of the item from the list\n")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10], 1, 2, 1, 2, 1, 2]

removed = 1

for i in list1:
    if removed in list1:
        list1.remove(1)

print(list1)
