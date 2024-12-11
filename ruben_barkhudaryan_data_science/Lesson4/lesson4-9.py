print("and / or vs & / |")

import numpy as np

print(bool(50000))
print(bool(0))

print(bool(42 and 0))
print(bool(42 or 0), "\n")

print(bin(42))
print(bin(59), "\n")

print(bin(42 & 59))
print(bin(42 | 59), "\n")

arr1 = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
arr2 = np.array([1, 1, 1, 0, 1, 1], dtype=bool)

print(arr1 | arr2)
# print(arr1 or arr2)
