print("Introducing Broadcasting")

import numpy as np

arr = np.array([0, 1, 2])
arr2 = np.array([5, 5, 5])

print(arr + arr2)
print(arr + 5)

matrix = np.ones((3, 3))

print(matrix)

print(matrix + arr)

arr = np.arange(3)
arr2 = np.arange(3)[:, np.newaxis]

print(arr)
print(arr2)

print(arr + arr2)
