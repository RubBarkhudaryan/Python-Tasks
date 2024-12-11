print("Modifying values with fancy indexing")

import numpy as np

x = np.zeros(10)

x[[0, 0]] = [4, 6]

print(x)
