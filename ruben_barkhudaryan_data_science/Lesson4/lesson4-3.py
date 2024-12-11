print("Broadcasting Example 3")

import numpy as np

matrix = np.ones((3, 2))
arr = np.arange(3)

print(matrix)
print(arr)

print(arr[:, np.newaxis].shape)
print(matrix + arr[:, np.newaxis])
