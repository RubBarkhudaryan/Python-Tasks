print("Numpy structured arrays\n")

import numpy as np

name = ["Alice", "Bob", "Cathy", "Doug"]
age = [25, 35, 45, 55]
weigth = [58.59, 69.0, 78.7, 80.1]

data = np.zeros(
    4, dtype={"names": ("name", "age", "weight"), "formats": ("U10", "i4", "f8")}
)

print(data.dtype)
print()

data["name"] = name
data["age"] = age
data["weight"] = weigth

print(data)
print()

print(data["name"])
print(data[0])
print(data[-1])
print(data[-1]["name"])
print(data[data["age"] < 30]["name"])
