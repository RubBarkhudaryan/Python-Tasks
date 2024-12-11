print("Universal functions-ufunc")

import numpy as np

np.random.seed(0)

arr = np.arange(5)
print("arr = ", arr)
print("arr + 5 = ", arr + 5)
print("arr - 5 = ", arr - 5)
print("arr * 2 = ", arr * 2)
print("arr / 2 = ", arr / 2)
print("arr // 2 = ", arr // 2)
print("-arr = ", -arr)
print("arr ** 2 = ", arr**2)
print("arr % 2 = ", arr % 2)


print(-((0.5 * arr + 1) ** 2))
print(np.add(arr, 2))
