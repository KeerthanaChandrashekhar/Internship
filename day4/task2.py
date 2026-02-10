IDs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(IDs)
print("Unique user IDs are:", unique_users)

print("Is 'ID05' in unique_users?", "ID05" in unique_users)

#length

print("Total length of the original list is:", len(IDs))
print("Total unique IDs are:", len(unique_users))