import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from day_4.passport_processing_pt2 import Passport


def test_valid_byr():
    test_passport = Passport(byr='1930')
    assert test_passport.byr_is_valid() is True


def test_invalid_year_byr():
    test_passport = Passport(byr='1900')
    assert test_passport.byr_is_valid() is False
 
   
def test_valid_iyr():
    test_passport = Passport(iyr='2015')
    assert test_passport.iyr_is_valid() is True 

def test_valid_eyr():
    test_passport = Passport(eyr='2025')
    assert test_passport.eyr_is_valid() is True

def test_valid_hgt_cm():
    test_passport = Passport(hgt= "160cm")
    assert test_passport.hgt_is_valid() is True


def test_valid_hgt_in():
    test_passport = Passport(hgt= "67in")
    assert test_passport.hgt_is_valid() is True


def test_valid_hcl():
    test_passport = Passport(hcl="#999999")
    assert test_passport.hcl_is_valid() is True

def test_valid_ecl():
    test_passport = Passport(ecl="amb")
    assert test_passport.ecl_is_valid() is True

def test_valid_pid():
    test_passport = Passport(pid="123456789")
    assert test_passport.pid_is_valid() is True

def test_valid_cid():
    test_passport = Passport(cid="11111")
    assert test_passport.cid_is_valid() is True

def test_valid_passport_1():
    test_passport = Passport(
        iyr="2010",
        hgt="158cm",
        hcl="#b6652a",
        ecl="blu",
        byr="1944",
        eyr="2021",
        pid="093154719"
    )
    assert test_passport.is_valid() is True


def test_valid_passport_2():
    test_passport = Passport(
        iyr="2012",
        hgt="74in",
        hcl="#623a2f",
        ecl="grn",
        byr="1980",
        eyr="2030",
        pid="087499704"
    )
    assert test_passport.is_valid() is True


def test_valid_passport_3():
    test_passport = Passport(
        iyr="2010",
        hgt="158cm",
        hcl="#b6652a",
        ecl="blu",
        byr="1944",
        eyr="2021",
        pid="093154719"
    )
    assert test_passport.is_valid() is True


def test_valid_passport_4():
    test_passport = Passport(
        iyr="2010",
        hgt="158cm",
        hcl="#b6652a",
        ecl="blu",
        byr="1944",
        eyr="2021",
        pid="093154719"
    )
    assert test_passport.is_valid() is True