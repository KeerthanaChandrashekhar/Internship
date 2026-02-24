ratings = [5, 4, 3, 5, 2, 4, 5, 3, 1, 4]

average_rating = sum(ratings) / len(ratings)
print("Average Rating:", average_rating)

ratings_5 = []

for i in range(len(ratings)):
    if ratings[i] == 5:
        ratings_5.append(i)
print("Number of 5-star ratings:", len(ratings_5))

# Ratings Below Average 

below_average = []
for rating in ratings:
    if rating < average_rating:
        below_average.append(rating)
        
print("Ratings below average:", below_average)

# sorting the ratings in reverse order

ratings.sort(reverse=True)
print("Ratings sorted in descending order:", ratings)