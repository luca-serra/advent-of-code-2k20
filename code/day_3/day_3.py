"""
Day 3: Toboggan Trajectory

Goal: Count the number of obstacles (trees) encountered given a pattern and a slope.
"""

INPUT_FILE = "../../data/day_3.txt"

if __name__ == "__main__":

    input_list = [str(rule_and_password) for rule_and_password in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    len_pattern = len(input_list[0])
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    all_count_trees = []

    for slope in slopes:
        x = 0  # Horizontal coordinate
        count_trees = 0

        for y in range(0, len(input_list), slope[1]):
            pattern = input_list[y]
            if pattern[x] == "#":
                count_trees += 1
            x += slope[0]
            x %= len_pattern
        all_count_trees.append(count_trees)

        print(
            f"For slope = 'Right: {slope[0]} / Down: {slope[1]}', Number of trees encountered during the descent: {count_trees}"
        )

    product_all_trees = 1

    for count in all_count_trees:
        product_all_trees *= count

    print(f"The product of all the trees encountered is {product_all_trees}")
