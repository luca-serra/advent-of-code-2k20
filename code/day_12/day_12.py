"""
Day 12: Rain Risk

Goal: Simulate the navigation of a boat given a series of instructions.
"""
import utils
import operator
import math as ma

INPUT_FILE = "../../data/day_12.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    # Part 1
    navigation = {"N": 0, "E": 0, "D": 0}  # North / East coordinates and current direction

    for direction in input_list:
        start_character = direction[0]
        value = int(direction[1:])
        if start_character == "N":
            navigation["N"] += value
        elif start_character == "S":
            navigation["N"] -= value
        elif start_character == "E":
            navigation["E"] += value
        elif start_character == "W":
            navigation["E"] -= value
        elif start_character == "F":
            navigation["N"] += ma.sin(ma.pi * navigation["D"] / 180) * value
            navigation["E"] += ma.cos(ma.pi * navigation["D"] / 180) * value
        elif start_character == "L":
            navigation["D"] += value
            navigation["D"] %= 360
        elif start_character == "R":
            navigation["D"] -= value
            navigation["D"] %= 360

    print(
        "(Part 1) Manhattan distance between that location and the ship's starting position:",
        utils.manhattan_distance(navigation["N"], navigation["E"]),
    )

    # Part 2
    navigation = {"N": 0, "E": 0, "D": [10, 1]}  # North / East coordinates and current direction

    for direction in input_list:
        start_character = direction[0]
        value = int(direction[1:])
        if start_character == "N":
            navigation["D"][1] += value
        elif start_character == "S":
            navigation["D"][1] -= value
        elif start_character == "E":
            navigation["D"][0] += value
        elif start_character == "W":
            navigation["D"][0] -= value
        elif start_character == "F":
            navigation["E"] += navigation["D"][0] * value
            navigation["N"] += navigation["D"][1] * value
        elif start_character in ["L", "R"]:
            if value == 180:
                navigation["D"][0] *= -1
                navigation["D"][1] *= -1
            elif (start_character, value) in [("R", 90), ("L", 270)]:
                east = navigation["D"][0]
                navigation["D"][0] = navigation["D"][1]
                navigation["D"][1] = -east
            else:
                north = navigation["D"][1]
                navigation["D"][1] = navigation["D"][0]
                navigation["D"][0] = -north

    print(
        "(Part 2) Manhattan distance between that location and the ship's starting position:",
        utils.manhattan_distance(navigation["N"], navigation["E"]),
    )
