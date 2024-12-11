print("Concatenation of arrays")

import numpy as np

arr = np.arange(16).reshape((4, 4))

print(arr)

upper, lower = np.vsplit(arr, [2])

print(upper)
print(lower)

left, right = np.hsplit(arr, [2])

print(left)
print(right)
