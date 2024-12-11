print("Fast sorting in numpy")

import numpy as np

x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)

print(i)
print(x[i])
