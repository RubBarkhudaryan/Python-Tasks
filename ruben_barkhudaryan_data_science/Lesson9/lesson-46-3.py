print("Data Selection in DataFrame")
print("Ufuncs:Index Alignment in Series")
import numpy as np
import pandas as pd
area=pd.Series({'Alaska':1723337,'Texas':695662,
                'California':423967}, name='area')
population=pd.Series({'California':39538223,
                      'Texas':29145505,'Florida':21538187},
                     name='population')
print(population/area)

print(area.index.union(population.index))

A=pd.Series([2,4,6],index=[0,1,2])
B=pd.Series([1,3,5],index=[1,2,3])
print(A+B)
print(A.add(B,fill_value=0))
