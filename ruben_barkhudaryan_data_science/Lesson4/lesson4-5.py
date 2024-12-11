print("Comparison operator as ufuncs")

import numpy as np

matrix = np.array([1, 2, 3, 4, 5])

print(matrix < 3)
print(matrix > 3)
print(matrix <= 3)
print(matrix >= 3)
print(matrix != 3)
print(matrix == 3)
print(2 * matrix == (matrix**2))
print("*" * 50)

rng = np.random.RandomState(0)

m = rng.randint(10, size=(3, 4))

print(m)

print(m < 6)
print(np.less(m, 3))
