print("Working with Boolean operators")

import numpy as np

rng = np.random.RandomState(0)

matrix = rng.randint(10, size=(3, 4))

print(matrix)
print(np.sum((matrix > 2) & (matrix < 6)))


print("Number of 0 values : ", np.sum(matrix == 0))
print("Number of not 0 values : ", np.sum(matrix != 0))
print("Number of values more than 2 : ", np.sum(matrix > 2))
print(
    "Number of values more than 0 and less than 5: ",
    np.sum((matrix > 0) & (matrix < 5)),
)
