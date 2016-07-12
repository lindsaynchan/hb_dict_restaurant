def user_input_restaurant_rating():

    user_restaurant_name = raw_input("Please enter a restaurant name: ")
    #prompt user for restaurant name using raw_input
    user_restaurant_score = raw_input("Please enter a score for the restaurant: ")
    #prompt user for restaurant score using raw_input
    user_restaurant_input = tuple([user_restaurant_name,user_restaurant_score])
    #create tuple from user input
    return user_restaurant_input


def restaurant_ratings(filename):
    """Function returning dictionary that contains restaurant name and rating."""

    restaurant_score_file = open(filename)
    #open the file and save it to a variable
    restaurant_scores = {}
    #create empty dictionary that will contain restaurant = key and score = value

    for line in restaurant_score_file:
        line = line.rstrip()
        #rstrip of the line
        line = line.split(':')
        #split by :
        restaurant_scores[line[0]] = line[1]
        #use list index to add restaurant: value to the empty dictionary
    
    restaurant_scores = restaurant_scores.items()
    #turns restuarant_scores into a list of tuples  

    user_restaurant_add = user_input_restaurant_rating()
    #calling our user_input function and saving that output as a variable
    restaurant_scores.append(user_restaurant_add)
    #adding the user_input tuple to our original restaurant_scores list
    
    sorted_restaurant_scores = sorted(restaurant_scores)
    #this alphabetically sorts the list of tuples

    for restaurant_name, rating in sorted_restaurant_scores:
        #iterate through an alphabetically sorted list to get 
        #restaurant name and rating
        print "%s is rated at %s." % (restaurant_name, rating)
        #print out restaurant name and rating in a string

restaurant_ratings("scores.txt")

