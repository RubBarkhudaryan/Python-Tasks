print("Numpy array attributes")

import numpy as np

print(np.random.seed((0)))

print()

arr = np.random.randint(10, size=6)
print(arr, "\n")

arr2 = np.random.randint(0, 10, (3, 3))
print(arr2, "\n")

arr3 = np.random.randint(0, 10, (3, 4, 5))
print(arr3, "\n")

print("arr3 ndim: ", arr3.ndim)
print("arr3 shape: ", arr3.shape)
print("arr3 size: ", arr3.size)
print("arr3 dtype: ", arr3.dtype)
print("arr3 itemsize: ", arr3.itemsize)
print("arr3 nbytes: ", arr3.nbytes)
