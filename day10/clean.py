import pandas as pd

data = {
    "CustomerID": [101, 102, 102, 104, 104],
    "Name": ["Alice", "Bob", "Bob", "Charlie", "Alice"],
    "Purchase": [500, 300, 300, 700, 700]
}

df = pd.DataFrame(data)
print(df)

#print(df.duplicated())

print(df[df.duplicated()])

df_clean = df.drop_duplicates()
print(df_clean)

print(df.duplicated(subset="CustomerID"))

print(df.drop_duplicates(keep="last"))

print(df.drop_duplicates(keep=False))

