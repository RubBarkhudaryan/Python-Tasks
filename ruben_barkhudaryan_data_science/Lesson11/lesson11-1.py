print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("The Bad Way")

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

pop = pd.Series(populations, index=index)

print(pop)

print()

print(pop[("California", 2010):("Texas", 2010),])
 
print()

print(pop[(i for i in pop.index if i[1] == 2010)])