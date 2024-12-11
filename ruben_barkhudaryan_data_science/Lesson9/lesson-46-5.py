print("Data Selection in DataFrame")
print("Ufuncs:Operations Between DataFrames and Series")
import numpy as np
import pandas as pd
rng=np.random.default_rng(42)
A=rng.integers(10,size=(3,4))
print(A)

print(A-A[0])
