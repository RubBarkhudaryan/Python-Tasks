print("Data Types")
print("Tuples")
print("Modifying items in tuple1")
tup1=('a','b','c','d',[20,30,45])
print(tup1[4][2])
tup1[4][1]=300
print(tup1)
tup1[4][2]=[100,200,300]
tup1[4][2].append(600)
print(tup1)
