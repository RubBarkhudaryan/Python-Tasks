print('Data Visualization')
print('Basic plotting with matplotlib')
print('Plotting bar chart')
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('dataset/tips.csv')
x=data['day']
y=data['total_bill']
plt.bar(x,y)
plt.title("Tips Dataset")
plt.ylabel('Total Bill')
plt.xlabel('Day')

plt.show()
