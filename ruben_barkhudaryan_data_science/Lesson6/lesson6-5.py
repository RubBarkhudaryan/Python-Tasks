print("More advanced compound types\n")

import numpy as np

tp = np.dtype([("id", "i8"), ("mat", "f8", (3, 3))])

x = np.zeros(1, dtype=tp)

print(x[0])
print(x["mat"][0])
