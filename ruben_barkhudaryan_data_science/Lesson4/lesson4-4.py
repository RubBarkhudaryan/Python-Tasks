print("Broadcasting Example 4")

import numpy as np

arr = np.random.random((10, 3))
arrMean = arr.mean(0)

print(arrMean)

arrCentered = arr - arrMean

print(arrCentered)
print(arrCentered.mean(0))