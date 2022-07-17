import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import re

class HandBag:

    def __init__(self, description):
        """
        description represents the line defining the bag and its contents
        in order to initialize the object the line must be parsed and loaded into attributes
        """
        parsed_description = self.parse_description(description)
        self.outer_bag = parsed_description["outer_bag"]

        # these two would really be better as a dictionary from inner bag to its count but I don't want to break pt 1 or duplicate everything else
        self.inner_bags = parsed_description["inner_bags"]
        self.inner_bag_counts = parsed_description["inner_bag_counts"]


    def parse_description(self, description):
        """
        this will first split it on each number then split on spaces
        it'll assign the string of the first two words to the outer bag
        and it'll assign each remaining bag to the first two words following each number
        """
        description_split_on_numbers = re.split('[0-9]', description)
        outer_bag_description = description_split_on_numbers[0].split()
        outer_bag = outer_bag_description[0] + " " + outer_bag_description[1]
        inner_bags = []

        for i in range(1, len(description_split_on_numbers)):
            inner_bag_description = description_split_on_numbers[i].split()
            inner_bag = inner_bag_description[0] + " " + inner_bag_description[1]
            inner_bags.append(inner_bag)

        inner_bag_counts = re.findall("[0-9]", description)

        bag_info = {
            "outer_bag": outer_bag,
            "inner_bags": inner_bags,
            "inner_bag_counts": inner_bag_counts
        }

        return bag_info


        




