import matplotlib.pyplot as plt

# Categories
products = ["Laptop", "Mobile", "Tablet", "Monitor"]

# Values
sales = [50, 80, 30, 60]

# Create bar chart
plt.bar(products, sales)

# Add labels
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales per Product")

plt.show()

"""Types of Bar Charts
Vertical Bar Chart (plt.bar())
Horizontal Bar Chart (plt.barh())
Grouped Bar Chart
Stacked Bar Chart"""