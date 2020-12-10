"""
Day 10: Adapter Array

Goal: Compute the number of arrangements in a list.
"""

INPUT_FILE = "../../data/day_10.txt"

if __name__ == "__main__":

    input_list = [int(string) for string in open(INPUT_FILE).readlines()]

    input_list_sorted = sorted(input_list)
    input_list_sorted.append(input_list_sorted[-1] + 3)
    input_list_sorted.insert(0, 0)

    # Part 1
    count_difference_1 = 0
    count_difference_3 = 0
    possible_next_adapters = {}
    n = len(input_list_sorted)

    for i in range(n - 1):
        # (For part 1)
        if input_list_sorted[i + 1] - input_list_sorted[i] == 1:
            count_difference_1 += 1
        elif input_list_sorted[i + 1] - input_list_sorted[i] == 3:
            count_difference_3 += 1

        # (For part 2)
        possible_next_adapters[input_list_sorted[i]] = []
        for j in range(i + 1, min(n, i + 4)):
            if input_list_sorted[j] - input_list_sorted[i] <= 3:
                possible_next_adapters[input_list_sorted[i]].append(input_list_sorted[j])

    # Part 2
    memo_count_ways = {}  # Memoization for the following recursive function

    def count_ways(jolt_number):
        if jolt_number == input_list_sorted[-1]:
            return 1
        res = 0
        for value in possible_next_adapters[jolt_number]:
            if value in memo_count_ways:
                res += memo_count_ways[value]
            else:
                memo_count_ways[value] = count_ways(value)
                res += memo_count_ways[value]
        return res

    print(
        f"(Part 1) 1-jolt differences: {count_difference_1}, 3-jolt differences: {count_difference_3}.",
        f"Their product is {count_difference_1 * count_difference_3}",
    )
    print(f"(Part 2) Total number of distinct ways to arrange the adapters: {count_ways(0)}")
