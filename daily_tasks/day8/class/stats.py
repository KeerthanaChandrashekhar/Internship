import numpy as np

data = np.array([[10, 20, 30],
                  [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))



data = np.array([10, 20, 30, 40, 50])

median_value = np.median(data)

print("Median:", median_value)



data = np.array([10, 20, 30, 40, 50])

std_value = np.std(data)

print("Standard Deviation:", std_value)

print("Mean (axis=1):", np.mean(data, axis=1))
print("Median (axis=1):", np.median(data, axis=1))
print("Std Dev (axis=1):", np.std(data, axis=1))