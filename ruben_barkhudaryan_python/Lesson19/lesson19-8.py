print("Data Types")
print("List")
print("Exercise 6")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 1, 5, 6, 5, 4, 5, 6, 5, 2, 58, 8, 4, 12]

index = []

for i in range(len(list1)):
    if list1[i] == 5:
        index.append(i)
        
count = len(index)

print("Count of 5 in list1 => " ,count)
print(index)