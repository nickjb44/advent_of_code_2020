import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from numpy import inner
import HandBag as hb
import utils

def get_n_of_target_bag(input_file, target_bag):
    """
    1. generate a lookup of all of the bags and their object/node
    2. perform a DFS on every bag to search for presence of the target bag somewhere down the line
    -- ideally this would be cached in some memoized or clever DP way but I don't really know how right now and that level of optimization is unnecessary here
    ---- One way might be to store whether there's a golden bag within each bag while calculating and use that to reduce duplicated calculations
    """

    bag_lookup = utils.generate_bag_lookup(input_file)
    target_count = 0

    for bag_name in bag_lookup:
        bag_contains_target = bag_DFS(bag_lookup, bag_lookup[bag_name], target_bag)
        if bag_contains_target:
            target_count += 1
    
    return target_count


def bag_DFS(bag_lookup, current_bag, target_bag):
    """
    This will recursively call all inner bags, searching for a target bag
    Once it finds it we'll pass up whether it's been found anywhere
    """
    target_bag_found = False
    for bag_name in current_bag.inner_bags:
        if bag_name == target_bag:
            target_bag_found = True
            # could also truncate search here by returning that we've found the target bag

        else:
            # recurse downward on each bag
            inner_bag = bag_lookup[bag_name]
            inner_bag_contains_target = bag_DFS(bag_lookup, inner_bag, target_bag)
            if inner_bag_contains_target:
                target_bag_found = True
                # could also truncate search here by returning that we've found the target bag

    # if we fail to find it in any of these DFS steps target bag found will still be false
    return target_bag_found
        

if __name__ == "__main__": 
    file = "./bag_rules.txt"
    print(get_n_of_target_bag(file, "shiny gold"))
