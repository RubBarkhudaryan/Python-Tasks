print("Creating copies of arrays")

import numpy as np

print(np.random.seed(0))

arr = np.random.randint(10, size=(3, 4))

arr_sub = arr[:2, :2]

arr_sub[0, 0] = 99

arr_sub_copy = arr[:2, :2].copy()

print(arr_sub_copy)

arr_sub_copy[0, 0] = 42

print(arr_sub_copy)

print(arr)