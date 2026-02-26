import numpy as np

pm_values = np.array([85, 90, 78, 120, 95, 130, 100])

average_pm = np.mean(pm_values)

unhealthy_days = pm_values[pm_values > 100]

percentage_unhealthy = (len(unhealthy_days) / len(pm_values)) * 100

print("PM2.5 values:", pm_values)
print("Average PM2.5 level:", average_pm)
print("Unhealthy PM2.5 values (above 100):", unhealthy_days)
print("Percentage of unhealthy days:", percentage_unhealthy, "%")