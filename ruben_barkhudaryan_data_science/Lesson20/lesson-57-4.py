print('Data Visualization')
print('Basic plotting with matplotlib')
print('Plotting scatter plot')
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('dataset/tips.csv')
x=data['day']
y=data['total_bill']
plt.scatter(x,y)
plt.title("Tips Dataset")
plt.xlabel('Day')
plt.ylabel('Total Bill')

plt.show()
