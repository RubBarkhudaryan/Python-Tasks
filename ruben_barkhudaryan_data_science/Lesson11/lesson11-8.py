print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("Methods of MultiIndex Constructors")

import pandas as pd

df = pd.MultiIndex.from_arrays([["a", "a", "b", "b"], [1, 2, 1, 2]])

print(df)

df = pd.MultiIndex.from_tuples([[("a", 1), ("a", 2), ("b", 1), ("b", 2)]])

print("-" * 50)

print(df)

df = pd.MultiIndex.from_product([["a", "b"], [1, 2]])

print("-" * 50)

print(df)
