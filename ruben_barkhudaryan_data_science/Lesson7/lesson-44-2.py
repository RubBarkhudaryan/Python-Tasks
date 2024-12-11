print("Constructing Series Objects")
import numpy as np
import pandas as pd

print(pd.Series([2,4,6]))
print(pd.Series(5,index=[100,200,300]))
print(pd.Series({2:'a',1:'b',3:'c'}))
print(pd.Series({2:'a',1:'b',3:'c'},index=[3,2]))
      
