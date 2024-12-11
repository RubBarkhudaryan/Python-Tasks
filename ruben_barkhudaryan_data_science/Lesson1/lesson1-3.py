print("Numpy array attributes")

import numpy as np

print(np.random.seed((0)))

print()

arr = np.random.randint(10, size=6)
print(arr, "\n")

print(arr[0])
print(arr[5])
print(arr[-6])
print(arr[-1])

print()

arr2 = np.random.randint(10, size=(3, 4))
print(arr2, "\n")
print(arr2[0, 0])
print(arr2[2, 0])
print(arr2[2, -1])

arr2[0, 0] = 12
print(arr2)

arr[0] = 15.0564841
print(arr)