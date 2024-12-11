print("Data Visualization")
print("Matplotlib customization and styling")
print("Plotting histogram")
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("DataSets/tips.csv")
x = data["day"]
y = data["total_bill"]
font = {"family": "Comic Sans MS", "color": "darkred", "weight": "bold", "size": 22}

plt.bar(x, y, color="darkred", edgecolor="skyblue", linewidth=2)

plt.title("Tips Dataset", fontdict=font, loc="center", color="red")
plt.ylabel("Total Bill", fontdict=font, fontsize=25, color="orange")
plt.xlabel("Day", fontdict=font, fontsize=25, color="skyblue")
plt.show()
