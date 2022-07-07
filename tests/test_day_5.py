import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from day_5.BoardingPass1 import BoardingPass as BoardingPass1


def test_example_boarding_pass_1():
    test = BoardingPass1(chars = "FBFBBFFRLR")
    assert test.calc_seat_id() == 357


def test_example_boarding_pass_2():
    test = BoardingPass1(chars = "BFFFBBFRRR")
    assert test.calc_seat_id() == 567


def test_example_boarding_pass_3():
    test = BoardingPass1(chars = "FFFBBBFRRR")
    assert test.calc_seat_id() == 119


def test_example_boarding_pass_4():
    test = BoardingPass1(chars = "BBFFBBFRLL")
    assert test.calc_seat_id() == 820



