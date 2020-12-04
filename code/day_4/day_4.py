"""
Day 4: Passport Processing

Goal: Detect valid passports (certain attributes must be present in each passport
and respect a certain pattern)
"""
import re

INPUT_FILE = "../../data/day_4.txt"

if __name__ == "__main__":

    input_list = [str(rule_and_password) for rule_and_password in open(INPUT_FILE).readlines()]
    for i, string in enumerate(input_list):
        string = string.replace("\n", "")
        input_list[i] = string

    if input_list[-1] != "":
        input_list.append("")

    def hgt(x):
        """Return True if the 'hgt' format is valid"""
        res = False
        if x.endswith("cm"):
            height = x.replace("cm", "/").split("/")[0]
            if height.isdigit():
                if 150 <= int(height) <= 193:
                    res = True
        if x.endswith("in"):
            height = x.replace("in", "/").split("/")[0]
            if height.isdigit():
                if 59 <= int(height) <= 76:
                    res = True
        return res

    rules = {
        "byr": lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
        "iyr": lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
        "eyr": lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
        "hgt": hgt,
        "hcl": lambda x: bool(re.match(r"^#[a-f0-9]{6}$", x)),
        "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda x: bool(re.match(r"^[0-9]{9}$", x)),
    }

    count_valid_passports_part_1 = 0
    count_valid_passports_part_2 = 0

    passport_string = ""

    for string in input_list:
        if string != "":
            passport_string += " " + string

        else:
            count_terms = passport_string.count(" ")  # For part 1 (and 2)
            if "cid" in passport_string:
                count_terms -= 1
            if count_terms == 7:
                count_valid_passports_part_1 += 1
                count_rules_respected = 0  # For part 2
                passport_list = passport_string.replace(":", " ").split(" ")

                for i, string in enumerate(passport_list):
                    if string in rules.keys():
                        if rules[string](passport_list[i + 1]):
                            count_rules_respected += 1
                if count_rules_respected == 7:
                    count_valid_passports_part_2 += 1

            passport_string = ""

    print(f"(Part 1) Number of valid passports: {count_valid_passports_part_1}")
    print(f"(Part 2) Number of valid passports: {count_valid_passports_part_2}")
