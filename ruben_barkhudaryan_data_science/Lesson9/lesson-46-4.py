print("Data Selection in DataFrame")
print("Ufuncs:Index Alignment in DataFrames")
import numpy as np
import pandas as pd
rng=np.random.default_rng(42)
A=pd.DataFrame(rng.integers(0,20,(2,2)),
                columns=['a','b'])
print(A)
B=pd.DataFrame(rng.integers(0,10,(3,3)),
                columns=['a','b','c'])
print(B)
print(A+B)

print(A.add(B,fill_value=A.values.mean()))
