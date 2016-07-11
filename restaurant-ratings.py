def restaurant_ratings(filename):
    """Function returning restaurant name and rating."""

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

    for restaurant_name, rating in sorted(restaurant_scores):
        #iterate through an alphabetically sorted list to get 
        #restaurant name and rating
        print "%s is rated at %s." % (restaurant_name, rating)
        #print out restaurant name and rating in a string

restaurant_ratings("scores.txt")