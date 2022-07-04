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

        return not any([param is None for param in relevant_params])

    
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

print(f"there are {count_valid_passports('example.txt')[0]} valid passports in the example file")
print(f"there are {count_valid_passports('test.txt')[0]} valid passports in the test file, and {count_valid_passports('test.txt')[1]}, total passports")