print()
print("Data Types")

print()
print("Complex Data Types")

print()
print("List")

print()

list1 = [1, 2.6, (45 + 67j), "hello", [1, 2, 3], 58, 78, True]

print("There are", len(list1), "items in list1 =", list1)
print()
print("The type of", list1, "is", type(list1))
print()

list2 = list((1, 2, 3, 4, False, True, False))
list3 = list(("one", "two", "three"))

print("There are", len(list2), "items in list2 =", list2)
print()
print("The type of", list2, "is", type(list2))
print()
print("There are", len(list3), "items in list3 =", list3)
print()
print("The type of", list3, "is", type(list3))
print()
print(list1[4][2])

list2[4] = "hello"
print(list2)

list1[4][0] = 10
list1[4][1] = 20
list1[4][2] = 30
print(list1)

print()
