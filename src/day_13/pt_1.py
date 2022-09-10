
def is_valid_bus_time(timestamp, bus_number):
    return timestamp % bus_number == 0

def calculate_code(timestamp, start_time, bus_number):
    diff = timestamp - start_time
    return diff * bus_number

def try_to_get_code_for_timestamp(timestamp, start_time, buses):
    for bus_number in buses:
        if is_valid_bus_time(timestamp, bus_number):
            return calculate_code(timestamp, start_time, bus_number)
    return -1

def parse_input(file):
    bus_info = {
        "start_time" : None,
        "buses" : None
    }
    data = [x.rstrip() for x in open(file, 'r')]
    start_time = int(data[0])
    buses = data[1].split(',')
    bus_info["start_time"] = start_time
    bus_info["buses"] = buses
    return bus_info
    


def brute_force_try_all(file):
    bus_info = parse_input(file)
    buses = bus_info["buses"]
    start_time = bus_info["start_time"]
    valid_buses = [int(bus) for bus in buses if bus != "x"]
    timestamp = start_time
    while True:
        timestamp_code = try_to_get_code_for_timestamp(timestamp, start_time, valid_buses)
        if timestamp_code != -1:
            return timestamp_code
        else:
             timestamp += 1

code = brute_force_try_all("input.txt")
print(code)
