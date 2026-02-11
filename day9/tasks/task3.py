import pandas as pd

usernames =  pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

clean_usernames = usernames.str.strip().str.lower()

print(" Cleaned Usernames:\n", clean_usernames)

contains_a = clean_usernames.str.contains('a')
print("\n Contains letter 'a':", contains_a)


