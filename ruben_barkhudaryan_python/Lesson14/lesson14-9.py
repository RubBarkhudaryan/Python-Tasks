print("Built-in functions.")
print("Getting the slice of elements from the collection")

str1 = ("a", "b", "c", "d", "e", "f", "g", "h")

str2 = slice(5)
print(str1[str2])

str3 = slice(1, 6, 3)
print(str1[str3])

str4 = slice(2, 8, 2)
print(str1[str4])
