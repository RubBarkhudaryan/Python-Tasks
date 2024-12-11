print("Combined Indexing")

import numpy as np

rand = np.random.RandomState(42)

x = np.arange(12).reshape((3, 4))

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

print(x)
print()

print(x[2, [2, 0, 1]])
print()

print(x[1:, [2, 0, 1]])
print()

mask = np.array([1, 0, 1, 0], dtype=bool)

print(x[row[:, np.newaxis], mask])
print()
