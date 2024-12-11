print("Data Selection in Series")
print("Series as one-dimensional array")
import numpy as np
import pandas as pd

data=pd.Series([0.25,0.5,0.75,1.0],
               index=['a','b','c','d'])
print(data['a':'c'])
print(data[0:2])
print(data[(data>0.3) & (data<0.8)]) 
print(data[['a','d']])
