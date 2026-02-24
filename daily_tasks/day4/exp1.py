details = {"friend_a" : {"name": "Bob", "city": "BLR", "favorite_food": "dosa"},
           "friend_b" : {"name": "Alice", "city": "Mumbai", "favorite_food": "Pani Puri"},
           "friend_c" : {"name": "Charlie", "city": "Bangalore"}}
print(details)

print("Favorite destination of friend_b is:", details["friend_b"]["city"])

details["friend_c"]["favorite_food"] = "Pizza"
print("Updated details:", details)

print("details of friend_a:", details["friend_a"])