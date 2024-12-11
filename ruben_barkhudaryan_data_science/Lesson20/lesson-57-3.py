print('Data Visualization')
print('Basic plotting with matplotlib')
print('Plotting histogram')
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('dataset/tips.csv')
x=data['total_bill']
plt.hist(x)
plt.title("Tips Dataset")
plt.ylabel('Frequency')
plt.xlabel('Total Bill')

plt.show()
