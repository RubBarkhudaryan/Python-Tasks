print("Multidimensional Aggregations")

import numpy as np

matrix = np.random.random((3, 4))

print(matrix)

print(matrix.sum())

print(matrix.sum(axis=0))
print(matrix.min(axis=0))
print(matrix.max(axis=0))
