print("Fancy Indexing")

import numpy as np

rand = np.random.RandomState(42)

x = np.arange(12).reshape((3, 4))

print(x)

print()

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print(x[row, col])

print()

print(x[row[:, np.newaxis], col])

print()

print(row[:, np.newaxis] * col)
