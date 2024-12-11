print("Concatenation of arrays")

import numpy as np

arr = [1, 2, 3, 4, 5, 6, 7, 8]

x1, x2, x3 = np.split(arr, [3, 5])

print(x1)
print(x2)
print(x3)