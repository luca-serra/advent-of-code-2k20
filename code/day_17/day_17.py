"""
Day 17: Conway Cubes

Goal: Similar to the Game of life, in 3 dimensions.
"""

import copy
import utils

INPUT_FILE = "../../data/day_17.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    # Part 1

    active_cubes = utils.initialization(input_list)

    for cycle in range(6):
        potential_active_cubes = utils.get_coordinates_to_observe(active_cubes)
        new_active_cubes = copy.copy(potential_active_cubes)
        for cube in potential_active_cubes:
            if not (utils.becomes_active(cube, active_cubes)):
                new_active_cubes.remove(cube)
        active_cubes = copy.copy(new_active_cubes)

    print(f"(Part 1) Number of remaining active cubes after 6 iterations: {len(active_cubes)}")
    print("Beginning of part 2, it may take a minute or so..")

    # Part 2

    active_cubes = utils.initialization_2(input_list)

    for cycle in range(6):
        potential_active_cubes = utils.get_coordinates_to_observe_2(active_cubes)
        new_active_cubes = copy.copy(potential_active_cubes)
        for cube in potential_active_cubes:
            if not (utils.becomes_active_2(cube, active_cubes)):
                new_active_cubes.remove(cube)
        active_cubes = copy.copy(new_active_cubes)

    print(f"(Part 2) Number of remaining active cubes after 6 iterations: {len(active_cubes)}")
