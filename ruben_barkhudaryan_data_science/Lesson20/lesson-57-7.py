print('Data Visualization')
print('Basic plotting with matplotlib')
print('Plotting heatmap')
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
data=np.random.rand(10,10)

plt.imshow(data, cmap='hsv',interpolation='sinc')
plt.colorbar()
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title("Example of Heatmap")

plt.show()
