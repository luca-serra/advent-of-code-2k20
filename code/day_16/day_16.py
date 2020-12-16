"""
Day 16: Ticket Translation

Goal: Identify tickets invalidity given a set of rules.
"""

import utils

INPUT_FILE = "../../data/day_16.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [
        string[:-1] for string in input_list if string != "\n"
    ]  # Deleting the '\n' character

    rules = {}
    valid_tickets = []
    is_nearby_ticket = False
    is_my_ticket = False
    unvalid_numbers = 0
    my_ticket = []

    for string in input_list:
        if ":" in string and string[-1] != ":":
            split = string.split(": ")
            rule = split[0]
            splited_range = split[1].replace(" or ", "-").split("-")
            ranges = [
                [int(splited_range[0]), int(splited_range[1])],
                [int(splited_range[2]), int(splited_range[3])],
            ]
            rules[rule] = ranges
        else:
            split_string = string.split(",")
            if is_my_ticket:
                my_ticket = [int(s) for s in split_string]
                is_my_ticket = False
            if is_nearby_ticket:
                ticket = [int(s) for s in split_string]
                ticket_is_valid = True
                for n in ticket:
                    unvalid_rules = 0
                    for rule in rules.values():
                        if not (utils.is_valid(n, rule)):
                            unvalid_rules += 1
                    if unvalid_rules == len(rules.keys()):
                        unvalid_numbers += n
                        ticket_is_valid = False
                if ticket_is_valid:
                    valid_tickets.append(ticket)
            if string.startswith("your"):
                is_my_ticket = True
            if string.startswith("nearby"):
                is_nearby_ticket = True

    print(f"(Part 1) Sum of unvalid numbers on nearby tickets: {unvalid_numbers}")

    # Part 2
    rules_positions = [
        list(rules.keys()) for idx in range(len(my_ticket))
    ]  # rules_positions[i]: candidate rules for the number at index i
    #  At the beginning, every rule is candidate then we reduce each time we see an incompatibility
    for ticket in valid_tickets:
        for i, number in enumerate(ticket):
            for rule_name, rule in rules.items():
                if not (utils.is_valid(number, rule)):
                    if rule_name in rules_positions[i]:
                        rules_positions[i].remove(rule_name)

    n_positions = len(rules_positions)
    for _ in range(n_positions):  # complexity in n ** 2
        for i in range(n_positions):
            if len(rules_positions[i]) == 1:
                for j in range(n_positions):
                    if j != i and rules_positions[i][0] in rules_positions[j]:
                        rules_positions[j].remove(rules_positions[i][0])

    result_part_2 = 1
    for i, number in enumerate(my_ticket):
        rule = rules_positions[i][0]
        if rule.startswith("departure"):
            result_part_2 *= number

    print(f"(Part 2) Multiplication of the 6 departure fields: {result_part_2}")
