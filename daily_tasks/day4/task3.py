friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

#Use the & operator to find interests they both share (Common interests).Union: Use the | operator to find a list of all unique interests between the two of them (All interests).Difference: Use the - operator to find interests that friend_a has but friend_b does not.Output: Print the results of the Shared, All, and Unique interests.
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
different_interests = friend_a - friend_b

print("Shared interests:", shared_interests)
print("All interests:", all_interests)
print("Interests that friend_a has but friend_b does not:", different_interests)

symmetric_difference = friend_a ^ friend_b
print("Interests that are unique to each friend:", symmetric_difference)


