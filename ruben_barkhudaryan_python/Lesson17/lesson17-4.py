print("Data Types")
print("List")
print("Accessing list items - indexing")

list1 = [1, 2, 3, 4, "5", "6", [7, 8], [9, 10]]

print(list1)
print(list1[3:5])
print(list1[:5:2])
print(list1[2::2])

print("\n-----------------\n")

print(list1[-len(list1) : -4])
print(list1[-len(list1) : -4 : 2])
print(list1[::-1])
