print("Handling Missing Data")
print("NaN as Sentinel Value")

import numpy as np
import pandas as pd

print(pd.Series([1, np.nan, 2, None]))

print()

x = pd.Series(range(2), dtype=int)

print(x)

print()

x[0] = None

print(x)
