print("Numpy multydimensional array slicing")

import numpy as np

print(np.random.seed((0)))

print()

arr2 = np.random.randint(10, size=(3, 4))

print(arr2)

print()

print(arr2[:2, :3])

print()

print(arr2[:3, ::2])

print()

print(arr2[::-1, ::-1])
