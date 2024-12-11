print("Numpy array slicing")

import numpy as np

print(np.random.seed((0)))

print()

arr = np.arange(10)
print(arr, "\n")

print(arr[:5])
print(arr[5:9])
print(arr[4:7])
print(arr[::2])
print(arr[1::2])
print(arr[::-1])
print(arr[5::-2])
