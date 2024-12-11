print("Universal functions ufunc - trigonometric functions")

import numpy as np

arr = np.array([1, 2, 4, 10])

print("arr = ", arr)


print("ln(arr)", np.log(arr))
print("log2(arr)", np.log2(arr))
print("log10(arr)", np.log10(arr))


print("*" * 50)

arr = [0, 0.001, 0.01, 0.1]

print("exp(arr) - 1 = ", np.expm1(arr))
print("log(1 + arr) = ", np.log1p(arr))
