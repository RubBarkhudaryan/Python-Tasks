print("Modifying values with fancy indexing")

import numpy as np

x = np.zeros(10)

index = np.array([2, 3, 3, 4, 4, 4])

x[index] += 1

print(x)
