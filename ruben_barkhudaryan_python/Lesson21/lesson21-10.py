print("Data Types")
print("Tuple")
print("Exercise 3")

tuple1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

prod = 1

for i in range(len(tuple1)):
    prod *= tuple1[i][i]
    
print("Prod = ", prod)