import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import HandBag as hb

def generate_bag_lookup(input_file):
    """
    This provides us with a mapping from the name of the bag to the object with the bag information
    it plays the role of linking the name to the node letting us traverse the network in a dfs without losing the names
    """
    bag_lookup = {}
    with open(input_file) as bag_rules:
        for bag_rule in bag_rules:
            bag = hb.HandBag(bag_rule)
            bag_name = bag.outer_bag
            bag_lookup[bag_name] = bag
    return bag_lookup
