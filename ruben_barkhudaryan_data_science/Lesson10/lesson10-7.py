print("Handling Missing Data")
print("NaN as Sentinel Value")
print("Filling Null Values")

import numpy as np
import pandas as pd

data = pd.Series([1, np.nan, 2, None, 3], index=list("abcde"), dtype="Int32")

print(data)

print()

print(data.fillna(0))

print()

print(data.fillna(method="ffill"))
