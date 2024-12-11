print("Universal functions ufunc - absolute value")

import numpy as np

arr = np.array([-2, -1, 0, 1, 2])

print(abs(arr))

print(np.absolute(arr))

print(np.abs(arr))


arr = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])

print(np.abs(arr))
