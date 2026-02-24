import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.subplot(1,2,1)
plt.bar(categories, sales)
plt.title("Sales by Category")

plt.subplot(1,2,2)
plt.plot(categories, sales)
plt.title("Sales Trend")

plt.tight_layout()
plt.show()