import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy.stats import zscore
import sqlite3 

file_path = r"C:\Users\keert\.cache\kagglehub\datasets\ruchikakumbhar\uber-dataset\versions\1\UberDataset.csv"

df = pd.read_csv(file_path)

df.head()
df.info()

df = df.dropna()
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
df = df.dropna(subset=['pickup_datetime'])



#Peak hour analysis
hourly_demand = df.groupby('hour').size()

plt.figure(figsize=(10,5))
hourly_demand.plot(kind='bar')
plt.title("Ride Demand by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Rides")
plt.show()

#Revenue Distribution
plt.figure(figsize=(8,5))
df['fare_amount'].hist(bins=50)
plt.title("Fare Amount Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

#Skewness
print("Skewness:", df['fare_amount'].skew())

#Revenue by Hour
hourly_revenue = df.groupby('hour')['fare_amount'].sum()

plt.figure(figsize=(10,5))
hourly_revenue.plot(kind='bar')
plt.title("Revenue by Hour")
plt.xlabel("Hour")
plt.ylabel("Total Revenue")
plt.show()

#z_score
df['z_score'] = zscore(df['fare_amount'])

expensive_rides = df[df['z_score'] > 3]

print("Number of unusually expensive rides:", len(expensive_rides))

#Sampling hourly mean fare distribution
sample_means = []

for i in range(1000):
    sample = df['fare_amount'].sample(100)
    sample_means.append(sample.mean())

plt.figure(figsize=(8,5))
pd.Series(sample_means).hist(bins=30)
plt.title("Sampling Distribution of Mean Fares")
plt.xlabel("Mean Fare")
plt.ylabel("Frequency")
plt.show()

#Revenue by week
day_revenue = df.groupby('day_of_week')['fare_amount'].sum()

plt.figure(figsize=(10,5))
day_revenue.plot(kind='bar')
plt.title("Revenue by Day of Week")
plt.xlabel("Day")
plt.ylabel("Total Revenue")
plt.show()

#Insights
peak_hour = hourly_demand.idxmax()
max_revenue_hour = hourly_revenue.idxmax()

print("Peak Demand Hour:", peak_hour)
print("Highest Revenue Hour:", max_revenue_hour)
print("Fare Skewness:", df['fare_amount'].skew())

conn = sqlite3.connect('ride_sharing_db')
cursor = conn.cursor()

df.to_sql("trips", conn, if_exists="replace", index=False)

#Peak Hour Revenue
query = """
SELECT hour, SUM(fare_amount) AS total_revenue
FROM trips
GROUP BY hour
ORDER BY total_revenue DESC
"""

peak_revenue = pd.read_sql(query, conn)

print(peak_revenue.head())

#Top Peak Hour
query_top = """
SELECT hour, SUM(fare_amount) AS total_revenue
FROM trips
GROUP BY hour
ORDER BY total_revenue DESC
LIMIT 1
"""

top_hour = pd.read_sql(query_top, conn)

print("Peak Revenue Hour:")
print(top_hour)

conn.close()