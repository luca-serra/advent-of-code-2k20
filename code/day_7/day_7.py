"""
Day 7: Handy Haversacks

Goal: Represent the bags inclusions given certain written rules.
"""

INPUT_FILE = "../../data/day_7.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    insertions = {}
    for string in input_list:
        string = (
            string.replace("no other", "0 other")
            .replace(",", "")
            .replace(".", "")
            .replace(" ", "")
            .replace("contain", "")
        )
        raw_list = string.replace("bags", "bag").split("bag")
        container_color = raw_list[0]
        insertions[container_color] = []
        for bag in raw_list[1:]:
            if len(bag) > 0:
                insertions[container_color].append((bag[0], bag[1:]))
    # Part 1

    all_colors = []
    count_bags = 0
    count_bags_previous = -1
    contained_colors_previous = ["shinygold"]
    contained_colors = []

    while count_bags_previous != count_bags:
        count_bags_previous = count_bags
        for color in contained_colors_previous:
            for key, value in insertions.items():
                if color in [tuple[1] for tuple in value] and not (key in contained_colors):
                    contained_colors.append(key)
        count_bags = len(contained_colors)
        all_colors += contained_colors
        contained_colors_previous = contained_colors
        contained_colors = []

    # Part 2

    def count_bags_within(color_tuples):
        """
        Recursive function to find the number of bags within a list of bags.
        colors tuples is a list of tuples: [(number1, color1), (number2, color2), ...]
        """
        score = 0
        for color_tuple in color_tuples:
            n = int(color_tuple[0])
            if n != 0:
                score += n * (1 + count_bags_within(insertions[color_tuple[1]]))
            else:
                pass
        return score

    print(f"(Part 1) Number of bags containing the 'shiny gold' bag: {len(set(all_colors))}")
    print(
        (
            "(Part 2) Number of bags within the 'shiny gold' bag: "
            f"{count_bags_within([(1, 'shinygold')]) - 1}"
        )
    )
