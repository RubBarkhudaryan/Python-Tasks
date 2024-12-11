print("Hierarchical Indexing")
print("Multiply Indexed Series")
print("The Better Way - Pandas MultiIndex as Extra Dimension")

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

print("-" * 50)

print(pop)

print("-" * 50)

print(pop[:, 2020])

print("-" * 50)

pop_df = pd.DataFrame(
    {
        "total": pop,
        "under18": [455454, 787878778, 21212121, 5656665656, 781200512, 23232354012],
    }
)

print(pop_df)

print("-" * 50)

f_u18 = pop_df["under18"] / pop_df["total"]

print(f_u18.unstack())
