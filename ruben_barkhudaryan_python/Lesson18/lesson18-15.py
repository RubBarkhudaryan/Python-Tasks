print("Data Types")
print("List")
print("Nested list")

list1 = [[9, 5, 4, 2, 11], [8, 1, 7, 6, 3]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j])