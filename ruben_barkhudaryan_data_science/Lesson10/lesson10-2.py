print("Handling Missing Data")
print("NaN as Sentinel Value")

import numpy as np

val = np.array([1, np.nan, 2, 3])

print(val)

print(val.dtype)

print(val.sum())  # -> error

print(99 + np.nan)

print(val.sum(), val.min(), val.max())

print(np.nansum(val), np.nanmin(val), np.nanmax(val))
