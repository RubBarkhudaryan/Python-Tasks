print("Data Types")
print("List")
print("Exercise 2")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = []

list3 = [var for var in range(len(list1)) if list1[var] % 2 == 1]

for i in range(len(list1)):
    if list1[i] % 2 == 1:
        list2.append(i)
        
print(list2)
print(list3)