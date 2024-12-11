print("Aggregations - min, max, etc.")

import numpy as np

arr = np.arange(1, 6)

print(arr)

num = np.random.random(100)

print(sum(num))

print(np.sum(num))

big_arr = np.random.rand(1000000)

print(min(big_arr), max(big_arr))
print(np.min(big_arr), np.max(big_arr))
print(big_arr.min(), big_arr.max())