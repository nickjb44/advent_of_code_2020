def is_valid_password(key, first_ind, second_ind, password):
    first_matches = password[first_ind - 1] == key
    second_matches = password[second_ind - 1] == key
    return xor(first_matches, second_matches)

def xor(first, second):
    return (first or second) and (not first or not second)

def parse_password_line(line):
    components = line.split()
    indices = components[0].split("-")
    key = components[1]
    key = key.replace(":","")
    password = components[2]
    password_info = {}
    password_info["key"] = key
    password_info["first_ind"] = int(indices[0])
    password_info["second_ind"] = int(indices[1])
    password_info["password"] = password
    return password_info


def count_valid_passwords(input_file):
    n_valid_passwords = 0
    with open(input_file, "r") as password_lines:

        for password_line in password_lines:
            password_info = parse_password_line(password_line)

            password_is_valid = is_valid_password(
                key=password_info["key"],
                first_ind=password_info["first_ind"],
                second_ind=password_info["second_ind"],
                password=password_info["password"])

            if password_is_valid:
                n_valid_passwords += 1
    
    return n_valid_passwords
                
print(f"there are {count_valid_passwords('example_passwords.txt')} valid passwords in the example")
print(f"there are {count_valid_passwords('passwords_with_rules.txt')} valid passwords in the input file")
 