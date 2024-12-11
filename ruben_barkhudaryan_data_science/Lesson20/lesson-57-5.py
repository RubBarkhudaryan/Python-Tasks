print('Data Visualization')
print('Basic plotting with matplotlib')
print('Plotting pie plot')
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('dataset/tips.csv')
cars=['AUDI','BMW','FORD','TESLA','JAGUAR']
data=[23,10,35,15,12]
plt.pie(data, labels=cars)
plt.title("Car Data")

plt.show()
