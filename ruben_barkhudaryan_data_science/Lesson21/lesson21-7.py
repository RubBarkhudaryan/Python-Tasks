print("Data Visualization")
print("Matplotlib customization and styling")
print("Plotting Scatter Plot")
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("DataSets/tips.csv")
x = data["day"]
y = data["total_bill"]
font = {"family": "Comic Sans MS", "color": "darkred", "weight": "bold", "size": 22}

plt.scatter(
    x,
    y,
    c=data["size"],
    s=data["total_bill"],
    marker="D",
    alpha=0.5,
)

plt.title("Tips Dataset", fontdict=font, loc="center", color="red")
plt.ylabel("Frequency", fontdict=font, fontsize=25, color="orange")
plt.xlabel("Total Bill", fontdict=font, fontsize=25, color="skyblue")
plt.show()
