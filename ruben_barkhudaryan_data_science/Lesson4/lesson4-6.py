print("Working with Boolean arrays")

import numpy as np

rng = np.random.RandomState(0)

matrix = rng.randint(10, size=(3, 4))

print(matrix)
print(np.count_nonzero(matrix < 6))
print(np.sum(matrix < 6))
print(np.sum(matrix < 6, axis=1))
print(np.sum(matrix < 6, axis=0))

print(np.any(matrix > 8))
print(np.any(matrix < 0))
print(np.all(matrix < 10))
print(np.all(matrix == 6))
print(np.all(matrix < 8, axis=1))
