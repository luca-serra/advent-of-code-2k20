"""
Day 13: Shuttle Search

Goal: Find matching time stamps for bus departure based on rules.
"""
import numpy as np
import utils

INPUT_FILE = "../../data/day_13.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    earliest_timestamp = int(input_list[0])
    bus_ids_raw = input_list[1].split(",")
    bus_ids = []
    for bus_id in bus_ids_raw:
        if bus_id != "x":
            bus_ids.append(int(bus_id))

    earliest_buses = []
    for bus_id in bus_ids:
        earliest_buses.append(utils.closest_greater_number(bus_id, earliest_timestamp))

    earliest_bus_id = bus_ids[np.argmin(earliest_buses)]
    waiting_time = min(earliest_buses) - earliest_timestamp
    print(
        "(Part 1)",
        f"ID of the earliest possible bus: {earliest_bus_id}.",
        f"The waiting time is: {waiting_time}.",
        f"The product is {waiting_time * earliest_bus_id}",
    )

    buses = []
    for i, bus_id in enumerate(bus_ids_raw):
        if bus_id != "x":
            buses.append((int(bus_id), i))

    bus_ids_part_2 = [tuple[0] for tuple in buses]
    bus_gaps = [tuple[1] for tuple in buses]

    timestamp_solution = bus_ids_part_2[0]
    lcm = bus_ids_part_2[0]
    for i in range(1, len(bus_ids_part_2)):
        while (timestamp_solution + bus_gaps[i]) % bus_ids_part_2[i] != 0:
            timestamp_solution += lcm
        lcm = utils.lcm(lcm, bus_ids_part_2[i])

    print(f"(Part 2) Earliest timestamp that matches the conditions: {timestamp_solution}")
