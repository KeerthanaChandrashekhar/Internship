import pandas as pd

names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print(names)

#convert to lower
print(names.str.lower())

print(names.str.contains('a'))

#Case-Insensitive Search
print(names.str.contains('a', case=False))

#remove whitespace
s = pd.Series(['  data ', ' science ', 'ML  '])
print(s.str.strip())

#Replace text
emails = pd.Series(['user@gmail.com', 'admin@yahoo.com'])
print(emails.str.replace('gmail', 'outlook', regex=False))

#get length
print(names.str.len())