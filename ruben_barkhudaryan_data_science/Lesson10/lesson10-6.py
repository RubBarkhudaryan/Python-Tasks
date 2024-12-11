print("Handling Missing Data")
print("NaN as Sentinel Value")
print("Dropping Null Values")

import numpy as np
import pandas as pd

# data = pd.Series([1, np.nan, "hello", None])

# print(data.dropna())

print()

df = pd.DataFrame([[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]])

# print(df)

# print()

# print(df.dropna())

# print()

# print(df.dropna(axis="columns"))

df[3] = np.nan

print(df)
print()

print(df.dropna(axis="columns", how="all"))
print()

print(df.dropna(axis="rows", thresh=3))
print()
