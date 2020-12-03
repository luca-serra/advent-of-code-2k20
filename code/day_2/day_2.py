"""
Day 2: Password Philosophy

Goal: Detect password which match to a certain rule.
"""

INPUT_FILE = "../../data/day_2.txt"

if __name__ == "__main__":

    valid_passwords_part_1 = 0
    valid_passwords_part_2 = 0

    input_list = [str(rule_and_password) for rule_and_password in open(INPUT_FILE).readlines()]

    for rule_and_password in input_list:
        rule = rule_and_password.split(": ")[0]
        password = rule_and_password.split(": ")[1]

        split = rule.replace("-", " ").split()
        first_digit_rule = int(split[0])
        second_digit_rule = int(split[1])
        letter = split[2]

        # For part 1

        n_occurence_letter = password.count(letter)
        if n_occurence_letter >= first_digit_rule and n_occurence_letter <= second_digit_rule:
            valid_passwords_part_1 += 1

        # For part 2

        count_correct_position = 0
        if password[first_digit_rule - 1] == letter:
            count_correct_position += 1
        if password[second_digit_rule - 1] == letter:
            count_correct_position += 1

        if count_correct_position == 1:
            valid_passwords_part_2 += 1

    print(
        "\n"
        + f"(Part 1) There are {valid_passwords_part_1} valid passwords out of {len(input_list)}\n"
    )
    print(
        f"(Part 2) There are {valid_passwords_part_2} valid passwords out of {len(input_list)}\n"
    )
