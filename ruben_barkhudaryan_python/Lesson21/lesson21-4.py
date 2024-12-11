import itertools

print("Data Types")
print("Tuples")
print("Concating tuples with itertools chain()")

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
tuple3 = tuple(item for item in itertools.chain(tuple1, tuple2))

print(tuple1)
print(tuple2)
print(tuple3)
