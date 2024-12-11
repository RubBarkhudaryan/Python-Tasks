print("Task 6\n")

import random

matrix = []

length = 4

for i in range(length):
    lst = []
    for j in range(length):
        lst.append(random.randint(1, 10))
    matrix.append(lst)

print(matrix)

sum_ = 0

for i in range(length):
    for j in range(length):
        sum_ += matrix[i][j]

print(f"Sum of elements of matrix is - {sum_}")
