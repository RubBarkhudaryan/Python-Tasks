print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("Methods of MultiIndex Creation")

import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.rand(4, 2),
    index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
    columns=["data1", "data2"],
)

print(df)

print()

data = {
    ("California", 2010): 37253956,
    ("California", 2020): 487844759,
    ("New York", 2010): 123549,
    ("New York", 2020): 78545421,
    ("Texas", 2010): 7810520,
    ("Texas", 2020): 369548712,
}


print(pd.Series(data))
