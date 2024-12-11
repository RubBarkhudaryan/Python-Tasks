print("Data Visualization")
print("Matplotlib customization and styling")
print("Plotting heatmap")
import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)

font = {"family": "Comic Sans MS", "color": "darkred", "weight": "bold", "size": 22}

plt.title("Linear graph", fontdict=font, loc="center", color="red")
plt.ylabel("Y-Axis", fontdict=font, fontsize=25, color="orange")
plt.xlabel("X-Axis", fontdict=font, fontsize=25, color="skyblue")
plt.ylim(0, 80)
plt.legend(["GFG", "M&Ms"], bbox_to_anchor=(1, 1), ncol=1)
plt.show()
