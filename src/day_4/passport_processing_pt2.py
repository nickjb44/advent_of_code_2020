import re

class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid


    def is_valid(self):
        """
        checks that all passport attributes have values (i.e. aren't none) except for cid
        """
        relevant_params = [
        self.byr,
        self.iyr,
        self.eyr,
        self.hgt,
        self.hcl,
        self.ecl,
        self.pid
        ]

        has_required_fields = not any([param is None for param in relevant_params])

        if not has_required_fields:
            # this sidesteps adding a null check to every single field, though that would probably be better
            return False

        valid_byr = self.byr_is_valid()
        valid_iyr = self.iyr_is_valid()
        valid_eyr = self.eyr_is_valid()
        valid_hgt = self.hgt_is_valid()
        valid_hcl = self.hcl_is_valid()
        valid_ecl = self.ecl_is_valid()
        valid_pid = self.pid_is_valid()
        valid_cid = self.cid_is_valid()

        all_checks_pass = all(
            [
            has_required_fields,
            valid_byr,
            valid_iyr,
            valid_eyr,
            valid_hgt,
            valid_hcl,
            valid_ecl,
            valid_pid,
            valid_cid
            ]
        )
        return all_checks_pass

    def byr_is_valid(self, desired_length=4, min_year=1920, max_year=2002):
        """
        1. four digits 
        2. at least 1920
        3. at most 2002
        """
        right_length = len(self.byr) == desired_length
        reasonably_young = int(self.byr) >= min_year
        reasonably_old = int(self.byr) <= max_year
        return right_length and reasonably_young and reasonably_old

    
    def iyr_is_valid(self, desired_length=4, min_year=2010, max_year=2020):
        """
        1. four digits 
        2. at least 2010
        3. at most 2020
        """
        right_length = len(self.iyr) == desired_length
        reasonably_young = int(self.iyr) >= min_year
        reasonably_old = int(self.iyr) <= max_year
        return right_length and reasonably_young and reasonably_old


    def eyr_is_valid(self,  desired_length=4, min_year=2020, max_year=2030):
        """
        1. four digits
        2. at least 2020
        3. at most 2030
        """
        right_length = len(self.eyr) == desired_length
        reasonably_young = int(self.eyr) >= min_year
        reasonably_old = int(self.eyr) <= max_year
        return right_length and reasonably_young and reasonably_old


    def hgt_is_valid(self, min_cm_height=150, max_cm_height=193, min_in_height=59, max_in_height=76):
        """
        1. number followed by cm or in
        2. cm -> at least 150
        3. cm -> at most 193 
        4. in -> at least 59
        5. in -> at most 76
        """
        if not self.hgt:
            return False
        structure_is_valid = bool(re.match(r"^\d+[a-z][a-z]$", self.hgt))
        if not structure_is_valid:
            return structure_is_valid
        (height, unit) = (re.search(r"(\d+)([a-z][a-z])", self.hgt)).groups()
        height = int(height)
        unit_is_valid = True
        if unit == "cm":
            tall_enough = height >= min_cm_height
            short_enough = height <= max_cm_height
        elif unit == "in":
            tall_enough = height >= min_in_height
            short_enough = height <= max_in_height
        else:
            # this variable assignment is unnecessary and just to make the reasoning clear
            unit_is_valid = False
            return unit_is_valid
        
        # the other two checks have already been short circuted above to avoid errors down the line in parsing and assigning values
        return tall_enough and short_enough


    def hcl_is_valid(self):
        """
        1. starts with #
        2. followed by exactly six hex-valid characters (0-9 or a-f)
        """
        return bool(re.match(r"^#[0-9a-f]{6}$", self.hcl))
        
    def ecl_is_valid(self):
        """
        1. in the set of {amb, blu, brn, gry, grn, hzl, oth}
        """
        return self.ecl in {'amb','blu','brn','gry', 'grn','hzl','oth'}

    def pid_is_valid(self):
        """
        1. 9 digit number (including leading zeros)
        """
        return bool(re.match(r"^\d{9}$", self.pid))

    def cid_is_valid(self):
        """
        1. completely ignored
        """
        return True

def line_to_passport(line):
    """
    takes in a line formatted as a space delimited list of key value pairs
    produces a Passport object from these key-value pairs and returns it
    """
    parameter_dictionary = {key_val.split(":")[0]:key_val.split(":")[1] for key_val in line.split()}
    return Passport(**parameter_dictionary)


def count_valid_passports(file):
    """
    takes in a file, parses each line to a passport, evaluates validity keeping a count and returns that final count
    """
    n_valid_passports = 0
    n_passports = 0
    with open(file) as unparsed_passports:
        running_line = ""
        for line in unparsed_passports:

            # if we're still reading new lines with content add it to the list
            if line.rstrip():
                running_line += " " + line.rstrip()
            
            # now parse the builtrup line into a passport
            else:
                curr_passport = line_to_passport(running_line)
                n_passports += 1
                if curr_passport.is_valid():
                    n_valid_passports += 1
                # reset the running line
                running_line = ""

        # do this one more time for the last line (TODO: clean this up into a function so it's less messy as per DRY)
        curr_passport = line_to_passport(running_line)
        n_passports += 1
        if curr_passport.is_valid():
            n_valid_passports += 1


    return [n_valid_passports, n_passports]
