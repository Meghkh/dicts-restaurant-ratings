"""Restaurant rating lister."""


# put your code here
def rating_lister(data_file):
    """ Print alphabetically sorted restaurant ratings.

    """

    scores_list = open(data_file)

    ratings_dictionary = {}

    for line in scores_list:
        line = line.rstrip().split(":")

        ratings_dictionary[line[0]] = line[1]

    for key, value in sorted(ratings_dictionary.items()):

        print "{} is rated at {}.".format(key, value)

rating_lister("scores.txt")
