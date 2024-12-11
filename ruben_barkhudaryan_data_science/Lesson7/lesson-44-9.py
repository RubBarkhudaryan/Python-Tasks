print("Pandas Index as immutable array")
import numpy as np
import pandas as pd

ind=pd.Index([2,3,5,7,11])
print(ind[1])
print(ind[::2])
print(ind.size,ind.shape,ind.ndim,ind.dtype)
#ind[1]=0

