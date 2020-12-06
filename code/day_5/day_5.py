"""
Day 5: Binary Boarding

Goal: Analyze the number of a set of seats given a binary description.
"""

INPUT_FILE = "../../data/day_5.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    seat_IDs = []

    for seat_description in input_list:
        row_description = seat_description[:7]
        column_description = seat_description[7:]

        row_number = 0
        column_number = 0
        for i, letter in enumerate(row_description):
            if letter == "F":
                pass
            elif letter == "B":
                row_number += 2 ** (7 - (i + 1))

        for i, letter in enumerate(column_description):
            if letter == "L":
                pass
            elif letter == "R":
                column_number += 2 ** (3 - (i + 1))

        seat_IDs.append(int(row_number * 8 + column_number))

    print(f"(Part 1) The highest seat ID on a boarding pass is {max(seat_IDs)}")

    missing_seats = list(set([i for i in range(max(seat_IDs))]) - set(seat_IDs))

    for i in range(1, len(missing_seats)):
        if missing_seats[i] != missing_seats[i - 1] + 1:
            print(f"(Part 2) The seat ID of my boarding pass is {missing_seats[i]}")
            break
