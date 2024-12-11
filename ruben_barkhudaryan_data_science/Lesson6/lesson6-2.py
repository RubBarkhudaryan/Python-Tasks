print("Partial sorts: Partitioning")

import numpy as np

rand = np.random.RandomState(42)

x = rand.randint(0, 10, (4, 6))

np.partition(x, (0, 2), axis=1)
