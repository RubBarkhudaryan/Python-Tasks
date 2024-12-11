print("Data Selection in DataFrame")
print("Ufuncs:Index Preservation")
import numpy as np
import pandas as pd
rng=np.random.default_rng(42)
ser=pd.Series(rng.integers(0,10,4))
print(ser)

df=pd.DataFrame(rng.integers(0,10,(3,4)),
                columns=['A','B','C','D'])
print(df)
print(np.exp(ser))
print(np.sin(df*np.pi/4))
