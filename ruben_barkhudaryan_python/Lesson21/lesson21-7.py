print("Data Types")
print("Tuples")
print("Finding if all elements are true or false with all()")

tuple1 = (1, 2, 3, 4, "l", "j", True)
tuple2 = (5, 6, 7, "", True)
tuple3 = (0,"", False)
tuple4 = ()

print(all(tuple1))
print(all(tuple2))
print(all(tuple3))
print(all(tuple4))

print("\nFinding if any element is true or false with any()\n")

print(any(tuple1))
print(any(tuple2))
print(any(tuple3))
print(any(tuple4))