print("Data Types")
print("Tuples")
print("Finding an item with its value")
tup1=('a','b','c','d','e','f','e','f','g')
position=tup1.index('d')
print(position)
position=tup1.index('d',4)
print(position)
position=tup1.index('d',4,len(tup1))
print(position)
