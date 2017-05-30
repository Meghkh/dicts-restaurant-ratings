"""Restaurant rating lister."""


# put your code here
def print_sorted_ratings(data_file):
    """ Print alphabetically sorted restaurant ratings.
    """

    scores_list = open(data_file)
    ratings_dictionary = {}

    for line in scores_list:
        # strip, split and unpack into descriptive variables
        restaurant_name, restaurant_rating = line.rstrip().split(":")
        # add key and value pairs to ratings dictionary
        ratings_dictionary[restaurant_name] = restaurant_rating

    input_resturant = raw_input("Please enter new restaurant name: ").title()
    input_rating = raw_input("Please enter restaurant rating: ")
    while input_rating.isdigit() is False:
        input_rating = raw_input("Please enter restaurant rating (from 0 to 10): ")

    ratings_dictionary[input_resturant] = input_rating

    # sort dictionary based on keys and print
    for key, value in sorted(ratings_dictionary.items()):
        print "{} is rated at {}.".format(key, value)

print_sorted_ratings("scores.txt")
