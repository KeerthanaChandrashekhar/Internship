import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [30, 25, 20, 15]

#This creates a blank canvas (figure).
plt.figure(figsize=(8,4))

#plt.subplot(rows, columns, position)
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Increasing Trend")
#This plots the first graph in the left section.
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Decreasing Trend")
#Now we are selecting the second section (right side).

plt.tight_layout()
plt.show()