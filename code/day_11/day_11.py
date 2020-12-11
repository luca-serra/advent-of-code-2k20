"""
Day 11: Seating System

Goal: Simulate the evolution of seats occupation given an input grid and rules.
"""
import utils
import copy

INPUT_FILE = "../../data/day_11.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    m = len(input_list)
    n = len(input_list[0])

    parts = [1, 2]
    rules = {}
    rules[1] = (utils.get_adjacent_occupied_seats, 4)
    rules[2] = (utils.get_adjacent_occupied_seats_extended, 5)

    for part in parts:
        grid = copy.copy(input_list)
        new_grid = copy.copy(grid)
        changes = -1

        while changes != 0:
            changes = 0
            for i in range(m):
                for j in range(n):
                    adjacent_occupied = rules[part][0](grid, i, j)
                    if grid[i][j] == "L" and adjacent_occupied == 0:
                        new_grid[i] = new_grid[i][:j] + "#" + new_grid[i][j + 1 :]
                        changes += 1
                    elif grid[i][j] == "#" and adjacent_occupied >= rules[part][1]:
                        new_grid[i] = new_grid[i][:j] + "L" + new_grid[i][j + 1 :]
                        changes += 1
            grid = copy.copy(new_grid)

        print(f"(Part {part}) Number of occupied seats: {utils.count_occupied_seats(grid)}")
