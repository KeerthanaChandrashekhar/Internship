import pandas as pd

df = pd.read_excel('Student_Performance_Dataset.xlsx')
print(df.head())

s = pd.Series([10, 20, 30, 40])
print(s)

# Accessing a single column as Series
math_scores = df['MathScore']
print("Math Scores (Series):")
print(math_scores)

subset = df[['Name', 'MathScore', 'ScienceScore']]
print("Selected Columns ")
print(subset)

print("DataFrame type:", type(df))
print("Series type:", type(math_scores))
print(df.dtypes)

marks = pd.Series([85, 90, 78], index = ['Math', 'Science', 'English'])
print(marks)

print(marks[0])

print(marks['Science'])

print(marks[['Math', 'English']])

print(marks[0:2])

print(marks['Math':'Science'])
print(marks[0])

# SLICING - Using iloc to slice first 5 rows (position-based slicing)
print("First 5 records (Position-based Slicing using iloc):")
print(df.iloc[1:5])

print(df.iloc[0:2, 0:2])  # Rows 0–2, Columns 0–1

print(df.iloc[2, 1])  # Row 2, Column 1
