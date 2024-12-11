print("Concatenation of arrays")

import numpy as np

arr = np.array([1, 2, 3])

grid = np.array([[9, 8, 7], [6, 5, 4]])

print(np.vstack([arr, grid]))

arr2 = np.array([[1, 2], [3, 4]])

print(np.hstack([grid, arr2]))
