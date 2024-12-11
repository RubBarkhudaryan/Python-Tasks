print("Handling Missing Data")
print("NaN as Sentinel Value")
print("Detecting Null Values")

import numpy as np
import pandas as pd

data = pd.Series([1, np.nan, "hello", None])

print(data.isnull())
print(data[data.notnull()])
print(data[data.isnull()])