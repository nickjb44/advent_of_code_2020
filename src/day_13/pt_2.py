
def parse_input(file):
    bus_info = {
        "start_time" : None,
        "buses_and_offset" : None
    }
    data = [x.rstrip() for x in open(file, 'r')]
    start_time = int(data[0])
    buses = data[1].split(',')
    valid_buses_with_offset = []
    for i, bus in enumerate(buses):
        if bus != "x":
            valid_buses_with_offset.append(
                {
                    "bus": int(bus),
                    "offset": i
                }
            )
    
    bus_info["start_time"] = start_time
    bus_info["buses_and_offset"] = valid_buses_with_offset
            
    return bus_info


def is_valid_bus_time(timestamp, bus_number, offset):
    return (timestamp + offset) % bus_number== 0


def recursively_find_time(current_time, buses_and_offset, current_step_size):

    # going backward to avoid changing the iterations from mutating the array mid loop
    for i in reversed(range(len(buses_and_offset))):
        bus_and_offset = buses_and_offset[i]
        bus = bus_and_offset["bus"]
        offset = bus_and_offset["offset"]
        if is_valid_bus_time(current_time, bus, offset):
            current_step_size *= bus
            print(f"length of list is {len(buses_and_offset)} and i is {i}. time is {current_time} and step size is {current_step_size}")
            buses_and_offset.pop(i)

    if len(buses_and_offset) == 0:
        print(f"length of list is {len(buses_and_offset)} and i is {i}. time is {current_time} and step size is {current_step_size}")
        return current_time
    else:
        return recursively_find_time(current_time + current_step_size, buses_and_offset, current_step_size)

 
def find_when_celestial_buses_align(file):
    bus_info = parse_input(file)

    return recursively_find_time(bus_info["start_time"], bus_info["buses_and_offset"], 1)

print(f"the answer is {find_when_celestial_buses_align('./input.txt')}")

