print("Universal functions ufunc - trigonometric functions")

import numpy as np

arr = np.array([-2, -1, 0, 1, 2])

theta = np.linspace(0, np.pi, 3)

print(theta)

print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

print("*" * 50)

arr = [1, 0, 1]

print("arcsin(arr)", np.arcsin(arr))
print("arccos(arr)", np.arccos(arr))
print("arctan(arr)", np.arctan(arr))
