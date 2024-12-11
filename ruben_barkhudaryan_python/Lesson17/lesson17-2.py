print("Data Types")
print("List")

list1 = []
list2 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

print("The type of ", list1, " is ", type(list1))
print("The type of ", list2, " is ", type(list2))

list3 = list()
list4 = list((1, 2, 3, 4, 5))
set1 = set({1, 2, 3, 4, 5})
list5 = list(set1)

print("The type of ", list3, " is ", type(list3))
print("The type of ", list4, " is ", type(list4))
print("The type of ", list5, " is ", type(list5))
print("The type of ", set1, " is ", type(set1))

print("There are ", len(list2), " items in ", list2)
