print("Data Types")
print("Tuples")
print("Copying a tuple")

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple2 = tuple1

list1 = list(tuple2)
list1.append(10)

tuple2 = tuple(list1)
print(tuple1)
print(tuple2)
