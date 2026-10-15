import matplotlib.pyplot as plt

# Create a 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# 1. Line plot (Top-Left)
axs[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])
axs[0, 0].set_title("Line Chart")

# 2. Bar chart (Top-Right)
axs[0, 1].bar(["A", "B", "C"], [3, 7, 5])
axs[0, 1].set_title("Bar Chart")

# 3. Histogram (Bottom-Left)
axs[1, 0].hist([1, 2, 2, 3, 3, 3, 4], bins=4)
axs[1, 0].set_title("Histogram")

# 4. Scatter plot (Bottom-Right)
axs[1, 1].scatter([1, 2, 3, 4], [4, 3, 2, 1])
axs[1, 1].set_title("Scatter Plot")

# Adjust layout, add labels/legends as needed, and save
plt.tight_layout()
plt.savefig("four_charts.png")
plt.show()
