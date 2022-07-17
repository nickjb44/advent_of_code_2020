import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from numpy import inner
import HandBag as hb
import utils


def get_n_contained_by_target(input_file, target_name):
    """
    1. compute the bag lookup
    2. call DFS to generate the count
    """

    bag_lookup = utils.generate_bag_lookup(input_file)
    target_bag = bag_lookup[target_name]
    n_contained_in_target = bag_count_DFS(bag_lookup, target_bag)
    # I think it's one off due to counting the outermost bag but I'm not entirely sure
    return n_contained_in_target - 1


def bag_count_DFS(bag_lookup, current_bag):
    """
    This will recursively call all inner bags, searching for a target bag
    Once it finds it we'll pass up whether it's been found anywhere
    """
    n_contained = 1
    inner_bag_info = zip(current_bag.inner_bags, current_bag.inner_bag_counts)

    for bag_name, bag_count in inner_bag_info:
        bag = bag_lookup[bag_name]
        n_bags_inside_inner_bag = bag_count_DFS(bag_lookup, bag)
        n_bags_inside_type = n_bags_inside_inner_bag * int(bag_count)
        n_contained += int(n_bags_inside_type)
    
    return n_contained



            

if __name__ == "__main__": 
    file = "./bag_rules.txt"
    print(get_n_contained_by_target(file, "shiny gold"))
