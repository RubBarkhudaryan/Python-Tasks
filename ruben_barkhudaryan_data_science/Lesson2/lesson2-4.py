print("Reshaping arrays")

import numpy as np

print(np.random.seed(0))

grid = np.array([1, 2, 3])

grid.reshape((1, 3))

print(grid[np.newaxis, :])

grid = grid.reshape((3, 1))

print(grid[:, np.newaxis])
