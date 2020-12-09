"""
Day 9: Encoding Error

Goal: Find the numbers which do not respect a rule based on previous numbers.
"""

INPUT_FILE = "../../data/day_9.txt"

if __name__ == "__main__":

    input_list = [int(string) for string in open(INPUT_FILE).readlines()]

    # Part 1
    sums = {}  # memoization dictionary for sum of two numbers
    unvalid_number = -1

    for i in range(25, len(input_list)):
        is_valid = False
        for j in range(i - 25, i - 1):
            for k in range(j + 1, i):
                if (input_list[j], input_list[k]) in sums.keys():
                    sum = sums[(input_list[j], input_list[k])]
                else:
                    sum = input_list[j] + input_list[k]
                    sums[(input_list[j], input_list[k])] = sum
                    sums[(input_list[k], input_list[j])] = sum

                if sum == input_list[i]:
                    is_valid = True
                    break
            if is_valid:
                break
        if not (is_valid):
            unvalid_number = input_list[i]
            break

    # Part 2
    sum = 0
    idx_begin = 0
    idx_end = 1
    for k in range(idx_begin, idx_end + 1):
        sum += input_list[k]

    while sum != unvalid_number:
        if sum < unvalid_number:
            idx_end += 1
            sum += input_list[idx_end]
        elif sum > unvalid_number:
            sum -= input_list[idx_begin]
            idx_begin += 1

    contiguous_list = [input_list[k] for k in range(idx_begin, idx_end + 1)]
    min_number = min(contiguous_list)
    max_number = max(contiguous_list)

    print(f"(Part 1) The unvalid number is: {unvalid_number}")
    print(
        f"(Part 2) The weakness in the XMAS-encrypted list of numbers is: {min_number + max_number}"
    )
