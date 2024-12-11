print("Data Selection in DataFrame")
print("Ufuncs: Operations Between DataFrames and Series")

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
A = rng.integers(10, size=(3, 4))

print(A)

print()

print(A - A[0])

print("\n", "*" * 50)

df = pd.DataFrame(A, columns=["Q", "R", "S", "T"])

print(df)

print()

print(df - df.iloc[0])

print("\n", "*" * 50)

print(df.subtract(df["R"], axis=0))

half_row = df.iloc[0, ::2]

print()

print(half_row)

print(df - half_row)
