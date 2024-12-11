print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("Indexing and Slicing MultiIndex")
print("Multiply Indexed Series")

import numpy as np
import pandas as pd

index = [
    ("California", 2010),
    ("California", 2020),
    ("New York", 2010),
    ("New York", 2020),
    ("Texas", 2010),
    ("Texas", 2020),
]
populations = [37253956, 487844759, 123549, 78545421, 7810520, 369548712]

index = pd.MultiIndex.from_tuples(index)

pop = pd.Series(populations, index=index)
pop = pop.reindex(index)
pop.index.names = ["state", "year"]

# print("-" * 50)

# print(pop["California"])

# print("-" * 50)

# print(pop.loc["California":"New York"])

# print("-" * 50)

# print(pop[:, 2010])

# print("-" * 50)

# print(pop[pop > 22000000])

print(pop[["California","Texas"]])