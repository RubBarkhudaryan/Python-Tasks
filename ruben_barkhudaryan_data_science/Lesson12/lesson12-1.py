print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("MultiIndex Level Names")

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

print(pop)
