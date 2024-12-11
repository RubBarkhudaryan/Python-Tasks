print()
print("Data Types")

print()
print("Complex Data Types")

print()
print("Dictionary - associative array")
print()

dictionary1 = {1: "one", 2: "two", 3: "three"}
print("There are", len(dictionary1), "items in dictionary1 =", dictionary1)
print()
print("The type of", dictionary1, "is", type(dictionary1))
print()

dictionary2 = dict((("one", 1), ("two", 2), ("three", 3)))
print("There are", len(dictionary2), "items in dictionary2 =", dictionary2)
print()
print("The type of", dictionary2, "is", type(dictionary2))
print()


dictionary3 = dict((["one", 1], ["two", 2], ["three", 3]))
print("There are", len(dictionary3), "items in dictionary3 =", dictionary3)
print()
print("The type of", dictionary3, "is", type(dictionary3))
print()

dictionary4 = () #empty dict
print("There are", len(dictionary4), "items in dictionary4 =", dictionary4)
print()
print("The type of", dictionary4, "is", type(dictionary4))
print()


dictionary5 = dictionary4 #empty dict
print("There are", len(dictionary5), "items in dictionary5 =", dictionary5)
print()
print("The type of", dictionary5, "is", type(dictionary5))
print()