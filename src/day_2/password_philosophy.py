def is_valid_password(key, min_count, max_count, password):
    n_occurrences = 0
    for char in password:
        if char == key:
            n_occurrences += 1
            if n_occurrences > max_count:
                return False
    return n_occurrences >= min_count

def parse_password_line(line):
    components = line.split()
    min_max = components[0].split("-")
    key = components[1]
    key = key.replace(":","")
    password = components[2]
    password_info = {}
    password_info["key"] = key
    password_info["min"] = int(min_max[0])
    password_info["max"] = int(min_max[1])
    password_info["password"] = password
    return password_info


def count_valid_passwords(input_file):
    n_valid_passwords = 0
    with open(input_file, "r") as password_lines:
        for password_line in password_lines:

            password_info = parse_password_line(password_line)
            password_is_valid = is_valid_password(
                key=password_info["key"],
                min_count=password_info["min"],
                max_count=password_info["max"],
                password=password_info["password"])

            if password_is_valid:
                n_valid_passwords += 1
    
    return n_valid_passwords
                
print(f"there are {count_valid_passwords('example_passwords.txt')} valid passwords in the example")
print(f"there are {count_valid_passwords('passwords_with_rules.txt')} valid passwords in the input file")
            