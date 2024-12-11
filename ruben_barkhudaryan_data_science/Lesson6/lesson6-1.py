print("Partial sorts: Partitioning")

import numpy as np

x = np.array([784, 5, 6, 8, 9, 2, 3, 1, 4, 7, 6, 78, 9])

print(np.partition(x, (0, 3)))
