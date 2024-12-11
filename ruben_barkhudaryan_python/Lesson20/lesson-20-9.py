print("Data Types")
print("Tuples")
print("Adding and changing items in tuple1")
tup1=('a','b','c','d','e','f','e','f','g')
#tup1[2]='hello'
list1=list(tup1)
list1[4]='z'
list1.extend(['w','x','y'])
tup1=tuple(list1)
print(tup1)
