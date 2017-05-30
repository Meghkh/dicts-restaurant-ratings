"""Restaurant rating lister."""

def display_menu():
    """ Displays options for user interaction and takes input

    """

    print "Please select an option: "
    print "1 - Display restaurant and ratings"
    print "2 - Add new restaurant and rating"
    print "3 - Quit program"

    user_choice = raw_input("-->")

def print_sorted_dictionary(restaurant_dict):
    """ Print formatted dictionary

    """
    for key, value in sorted(restaurant_dict.items()):
        print "{} is rated at {}.".format(key, value)


def get_restaurant_from_user(restaurant_dict):
    """ Returns a dictionary with new input from user added.

    """

    input_resturant = raw_input("Please enter new restaurant name: ").title()
    input_rating = raw_input("Please enter restaurant rating: ")

    while not input_rating.isdigit():
        input_rating = raw_input("Please enter restaurant rating (from 0 to 10): ")

    restaurant_dict[input_resturant] = input_rating

    return restaurant_dict


def read_and_parse_data(data_file):
    """ Opens file, reads and parses data, and returns a dictionary.
    """

    scores_list = open(data_file)
    ratings_dictionary = {}

    for line in scores_list:
        # strip, split and unpack into descriptive variables
        restaurant_name, restaurant_rating = line.rstrip().split(":")
        # add key and value pairs to ratings dictionary
        ratings_dictionary[restaurant_name] = restaurant_rating

    scores_list.close()

    return ratings_dictionary


def run_program():
    """ Runs program for complete restaurant/rating experience

    """

    new_dict = {}

    while True:
        user_decision = display_menu
        new_dict = read_and_parse_data("scores.txt")
        new_dict = get_restaurant_from_user(new_dict)
        print_sorted_dictionary(new_dict)

run_program()
