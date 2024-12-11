print("Advanced ufunc features")

import numpy as np

arr = np.arange(5)

arr2 = np.empty(5)

print("arr = ", arr)
print("arr2 = ", arr2)

np.multiply(arr, 10, out=arr2)

print(arr2)