print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("MultiIndex Level Names")

import numpy as np
import pandas as pd

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=["year", "visit"])

columns = pd.MultiIndex.from_product(
    [["Bob", "Guido", "Sue"], ["HR", "Temp"]], names=["subject", "type"]
)

data = np.round(np.random.randn(4, 6), 1)

data[:, ::2] *= 10
data += 37
health_data = pd.DataFrame(data, index=index, columns=columns)

print(health_data)

print("-" * 50)

print(health_data["Guido"])
