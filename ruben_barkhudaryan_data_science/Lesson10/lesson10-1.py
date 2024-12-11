print("Handling Missing Data")
print("None as Sentinel Value")

import numpy as np

val = np.array([1, None, 2, 3])

print(val)

print(val.dtype)
# print(val.sum()) # -> error
