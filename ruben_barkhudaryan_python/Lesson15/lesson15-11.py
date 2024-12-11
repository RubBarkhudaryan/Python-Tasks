print("Math module")
print("Checking the closeness of two numbers")

import math

print(math.isclose(6, 7))
print(math.isclose(6.9999999999, 7))
print(math.isclose(6, 7, rel_tol=0.2))
print(math.isclose(6, 7, abs_tol=1.0))
print(math.isclose(6, 7, abs_tol=0.2))
print(math.isclose(1, 1.000000001, abs_tol=1e-08))
