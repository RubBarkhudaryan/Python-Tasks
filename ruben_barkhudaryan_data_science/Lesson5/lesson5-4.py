print("Modifying values with fancy indexing")

import numpy as np

rand = np.random.RandomState(42)

x = np.arange(12)
i = np.array([2, 1, 8, 4])

x[i] = 99 

print(x)
