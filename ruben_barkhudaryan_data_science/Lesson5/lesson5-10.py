print("Fast sorting in numpy")

import numpy as np

rand = np.random.RandomState(42)

x = rand.randint(0, 10, (4, 6))

print(x)

print()
print(np.sort(x, axis=0))

print()
print(np.sort(x, axis=1))
