print("More advanced compound types\n")

import numpy as np

name = ["Alice", "Bob", "Cathy", "Doug"]
age = [25, 35, 45, 55]
weigth = [58.59, 69.0, 78.7, 80.1]

data = np.zeros(
    4, dtype={"names": ("name", "age", "weight"), "formats": ("U10", "i4", "f8")}
)


data["name"] = name
data["age"] = age
data["weight"] = weigth

data_rec = data.view(np.recarray)

print(data_rec.name)
print(data_rec.age)
print(data_rec.weight)
