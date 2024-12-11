print("Data Types")
print("List")
print("Comprehension")


inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareList = [var**2 for var in inputList if var % 2 == 0]

print(squareList)
