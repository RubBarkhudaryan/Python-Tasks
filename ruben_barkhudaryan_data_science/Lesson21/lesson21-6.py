print("Data Visualization")
print("Matplotlib customization and styling")
print("Plotting histogram")
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("DataSets/tips.csv")
x = data["total_bill"]
font = {"family": "Comic Sans MS", "color": "darkred", "weight": "bold", "size": 22}

plt.hist(x, bins=25, color="darkred", edgecolor="skyblue", linestyle="--", alpha=0.5)

plt.title("Tips Dataset", fontdict=font, loc="center", color="red")
plt.ylabel("Frequency", fontdict=font, fontsize=25, color="orange")
plt.xlabel("Total Bill", fontdict=font, fontsize=25, color="skyblue")
plt.show()
