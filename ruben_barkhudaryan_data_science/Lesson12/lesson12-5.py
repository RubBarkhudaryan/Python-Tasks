print("Hierarchical Indexing")
print("Rearranging Multi-Indexing")
print("Sorted and Unsorted Indices")

import numpy as np
import pandas as pd

index = pd.MultiIndex.from_product([["a", "c", "b"], [1, 2]], names=["year", "visit"])

data = pd.Series(np.random.rand(6), index=index)

data.index.names = ["char", "int"]

# print(data)

# try:
#     data["a":"b"]
# except KeyError as e:
#     print("KeyError ", e)

data = data.sort_index()

print(data)

print()

print(data["a":"b"])
