import pandas as pd

df = pd.read_csv('customer_data.csv')
print("Orginal dataframe shape:", df.shape)

null_values = df.isna().sum()
print("Null values in each column:\n", null_values)

for col in df.select_dtypes(include="number"):
    df[col] = df[col].fillna(df[col].median())
    
df = df.drop_duplicates()
print("\nCleaned DataFrame:\n", df)
print("Cleaned dataframe shape:", df.shape)