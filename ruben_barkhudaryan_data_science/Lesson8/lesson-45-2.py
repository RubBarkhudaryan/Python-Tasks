print("Data Selection in Series")
print("Series as directory")
import numpy as np
import pandas as pd

data=pd.Series([0.25,0.5,0.75,1.0],
               index=['a','b','c','d'])
print(data)

print(data['b'])
print('a' in data)
print(data.keys())
print(list(data.items()))

