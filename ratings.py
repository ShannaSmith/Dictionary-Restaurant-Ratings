"""Restaurant rating lister."""


# put your code here
def rate_restaurant(filename):
    restaurant_list = open(filename)
    restaurant_ratings = {}
    for line in restaurant_list:
       line = line.rstrip()
       #print(line)
       restaurants, rating = line.split(":")
      # print(restaurants)
       restaurant_ratings[restaurants] = (rating)
      # print(restaurant_ratings)
    restaurants_view = restaurant_ratings.items()
    restaurants_rating_list = sorted(restaurants_view)
    print(restaurants_rating_list)
    return restaurants_rating_list
       
     

rate_restaurant("scores.txt")
