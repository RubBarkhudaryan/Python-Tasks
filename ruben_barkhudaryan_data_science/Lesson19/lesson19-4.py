print("Pandas: How to read write files")
print("Working with big data")
print("Forcing less precise data types")

import pandas as pd
import numpy as np

df = pd.read_csv("dataset/csv/data.csv", index_col=0, parse_dates=["IND_DAY"])

print(df.dtypes)
print()
print(df.memory_usage())

print(df.loc[:, ["POP", "AREA", "GDP"]].memory_usage(index=False).sum())
print(df.loc[:, ["POP", "AREA", "GDP"]].memory_usage().sum())

print(df.loc[:, ["POP", "AREA", "GDP"]].to_numpy().nbytes)
