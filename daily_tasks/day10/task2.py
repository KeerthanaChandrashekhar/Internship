import pandas as pd

data = {
    "Price": ["$10.50", "$20.00", "$15.75", "$30.25"],
    "Date": ["2024-01-01", "2024-01-05", "2024-01-10", "2024-01-15"]
}

df = pd.DataFrame(data)

print("Original data type: \n", df.dtypes)

df["Price"] = df['Price'].str.replace('$', '').astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nCleaned data type: \n", df.dtypes)