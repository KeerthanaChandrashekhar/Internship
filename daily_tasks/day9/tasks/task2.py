import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("\n", grades.isnull())

print("\n", grades.fillna(0))

mask = grades >= 60
print("\n", grades[mask])

