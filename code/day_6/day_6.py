"""
Day 6: Custom Customs

Goal: Couting the number of questions answered by group of people during custom declaration form.
"""

INPUT_FILE = "../../data/day_6.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character
    input_list.append("")  # Adding empty string at the end of the list to treat the last element

    count_questions_part_1 = 0
    count_questions_part_2 = 0

    questions_answered_part_1 = set()  # Total unique questions answered by a given group
    questions_answered_part_2 = set([-1])  # Total common unique questions answered by a given group

    for string_question in input_list:
        if string_question != "":
            questions_answered_part_1.update(list(string_question))
            if questions_answered_part_2 == set([-1]):
                questions_answered_part_2 = set(list(string_question))
            else:
                questions_answered_part_2 = questions_answered_part_2.intersection(
                    list(string_question)
                )
        else:  # A new group is considered
            count_questions_part_1 += len(questions_answered_part_1)
            count_questions_part_2 += len(questions_answered_part_2)
            questions_answered_part_1 = set()
            questions_answered_part_2 = set([-1])

    print(f"(Part 1) The sum of the counts of questions answered is {count_questions_part_1}")
    print(f"(Part 2) The sum of the counts of questions answered is {count_questions_part_2}")
