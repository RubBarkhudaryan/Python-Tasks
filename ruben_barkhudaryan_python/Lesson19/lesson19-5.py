print("Data Types")
print("List")
print("Exercise 2")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = []

list3 = [var for var in range(len(list1)) if list1[var] % 2 == 1]

for i in list1:
    if i % 2 == 1:
        ind = list1.index(i)
        index.append(ind)
        
print(index)
print(list3)