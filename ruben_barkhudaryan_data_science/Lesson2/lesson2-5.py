print("Reshaping arrays")

import numpy as np

arr = np.array([1, 2, 3])
arr2 = np.array([3, 2, 1])

print(np.concatenate([arr, arr2]))

arr3 = [99, 99, 99]

print(np.concatenate([arr, arr2, arr3]))

grid = np.array([[1, 2, 3], [4, 5, 6]])

print(np.concatenate([grid, grid]))

print(np.concatenate([grid, grid], axis=1))
