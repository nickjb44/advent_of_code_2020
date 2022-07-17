import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from day_7.HandBag import HandBag
import day_7.utils as utils
import day_7.pt_1 as pt_1



def test_parse_first_example_line():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    parsed = HandBag(line)
    assert parsed.outer_bag == "light red" and parsed.inner_bags[0] == "bright white" and parsed.inner_bags[1] == "muted yellow"


def test_parse_second_example_line():
    line = "dark orange bags contain 3 bright white bags, 4 muted yellow bags"
    parsed = HandBag(line)
    assert parsed.outer_bag == "dark orange" and parsed.inner_bags[0] == "bright white" and parsed.inner_bags[1] == "muted yellow"


def test_faded_blue_bags_example_file():
    file = "../src/day_7/test_1.txt"
    handbag_lookup = utils.generate_bag_lookup(file)
    faded_blue_bag = handbag_lookup["faded blue"]
    assert faded_blue_bag.outer_bag == "faded blue" and len(faded_blue_bag.inner_bags) == 0

def test_example_n_gold_bags():
    file = "../src/day_7/test_1.txt"
    n_found = pt_1.get_n_of_target_bag(file, "shiny gold")
    assert n_found == 4

