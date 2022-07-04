from passport_processing_pt2 import count_valid_passports

print(f"there are {count_valid_passports('example.txt')[0]} valid passports in the example file")
print(f"there are {count_valid_passports('test.txt')[0]} valid passports in the test file, and {count_valid_passports('test.txt')[1]}, total passports")
print(f"there are {count_valid_passports('four_invalid_passports.txt')[0]} valid passports in the test file, and {count_valid_passports('four_invalid_passports.txt')[1]}, total passports")
print(f"there are {count_valid_passports('four_valid_passports.txt')[0]} valid passports in the test file, and {count_valid_passports('four_valid_passports.txt')[1]}, total passports")