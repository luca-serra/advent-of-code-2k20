"""
Day 15: Rambunctious Recitation

Goal: Find the pattern numbers of a game given a start input list.
"""
import copy

INPUT_FILE = "../../data/day_15.txt"

if __name__ == "__main__":
    input = open(INPUT_FILE).readlines()[0]
    input_list = input.split(",")
    input_list = [int(string) for string in input_list]

    number_list = copy.copy(input_list)
    numbers = {}
    for i, number in enumerate(input_list):
        if number in numbers:
            numbers[number].append(i)
        else:
            numbers[number] = [i]

    idx_to_compute = 2020  # 30000000 for Part 2
    for i in range(len(input_list), idx_to_compute):
        # print("\r", i/idx_to_compute, end="")  to use for part 2, to see the progression
        number = number_list[-1]
        if len(numbers[number]) > 1:
            new_number = numbers[number][-1] - numbers[number][-2]
        else:
            new_number = 0

        if new_number in numbers:
            numbers[new_number] = numbers[new_number][-1:] + [i]
        else:
            numbers[new_number] = [i]
        number_list = number_list[-2:] + [new_number]

    print(f"{idx_to_compute}th number spoken: {number_list[-1]}")
