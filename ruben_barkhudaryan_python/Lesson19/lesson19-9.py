print("Data Types")
print("List")
print("Exercise 6")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = []

for i in range(len(list1)):
    index.append(list1.pop())
        
print(index)