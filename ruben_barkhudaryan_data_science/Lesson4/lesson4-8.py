print("Working with Boolean arrays as masks")

import numpy as np

rng = np.random.RandomState(0)

matrix = rng.randint(10, size=(3, 4))

print(matrix)

print(matrix < 5)

print(matrix[matrix < 5])
