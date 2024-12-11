print("Intro to Pandas\n")

import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.50, 0.75, 1.0])

print(data)
print()

print(data.values)
print()

print(data.index)
print()

print(data[1])
print()

print(data[1:3])
print()
