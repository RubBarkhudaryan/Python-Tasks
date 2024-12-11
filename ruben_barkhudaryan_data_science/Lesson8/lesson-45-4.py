print("Data Selection in Series")
print("Indexers: loc,iloc and ix")
import numpy as np
import pandas as pd

data=pd.Series(['a','b','c'], index=[1,3,5])
print(data)
print(data[1])
print(data[1:3])
print(data.iloc[1])
print(data.iloc[1:3])
print(data[1])
print(data.ix[1])
