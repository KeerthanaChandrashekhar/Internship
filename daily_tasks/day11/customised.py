import matplotlib.pyplot as plt 

months = [1, 2, 3, 4, 5]

sales = [100, 150, 200, 180, 220]

plt.plot(months, sales, label = "Sales")

plt.title("Monthly sales Report", fontsize = 14, color = "blue")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()