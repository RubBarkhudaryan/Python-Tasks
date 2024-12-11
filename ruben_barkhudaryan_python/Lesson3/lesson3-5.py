print()
print("Data Types")

print()
print("Complex Data Types")

print()
print("Set")
print()

set1 = {1, 2, 3, 4, 5, "hello", "bye", True, False, 3, 2, 1}
print("There are", len(set1), "items in set1 =", set1)
print()
print("The type of", set1, "is", type(set1))
print()


set2 = {"1", "2", "3", "4", "5", "hello", "bye", True, 3 + 3j, 4, 7, False}
print("There are", len(set2), "items in set2 =", set2)
print()
print("The type of", set2, "is", type(set2))
print()


set3 = set()  # empty set
print(type(set3))

set3 = {}  # empty set
print(type(set3))

set4 = {1, 2, 3, 4}
set5 = {5, 6, 7, 8}

set6 = set4 | set5
print(set6)
