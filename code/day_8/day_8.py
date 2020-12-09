"""
Day 8: Handheld Halting

Goal: Execute a list of instructions given certain rules.
"""

INPUT_FILE = "../../data/day_8.txt"

if __name__ == "__main__":

    input_list = [str(string) for string in open(INPUT_FILE).readlines()]
    input_list[-1] += "\n"
    input_list = [string[:-1] for string in input_list]  # Deleting the '\n' character

    instruction_indices = []
    end_of_program = False
    acc = 0
    idx = 0
    n = len(input_list)

    # Part 1
    while end_of_program is False:
        instruction_indices.append(idx)
        if len(set(instruction_indices)) != len(instruction_indices):
            end_of_program = True
            print(f"(Part 1) Instruction already executed, value of acc: {acc}")

        string = input_list[idx]
        number = int(string[5:])
        if string[4] == "-":
            number *= -1

        if string.startswith("acc"):
            acc += number
            idx += 1
        elif string.startswith("jmp"):
            idx += number
        else:  # starts with 'nop'
            idx += 1

    indices_nop = [
        i for i, x in enumerate(input_list) if x.startswith("nop")
    ]  # list of indices tried to be modified to get the program to work
    indices_jmp = [
        i for i, x in enumerate(input_list) if x.startswith("jmp")
    ]  # list of indices tried to be modified to get the program to work
    indices_to_try = indices_nop + indices_jmp
    proper_ending = False
    instruction_indices = []
    end_of_program = False
    acc = 0
    idx = 0

    # Part 2
    for ind in indices_to_try:
        if proper_ending:
            print(f"(Part 2) Proper ending, value of acc: {acc}")
            break
        end_of_program = False
        while end_of_program is False:
            instruction_indices.append(idx)
            if len(set(instruction_indices)) != len(instruction_indices):
                end_of_program = True
                acc = 0
                idx = 0
                instruction_indices = []

            string = input_list[idx]
            if idx == ind:
                if idx in indices_jmp:
                    string = "nop" + string[3:]
                elif idx in indices_nop:
                    string = "jmp" + string[3:]

            number = int(string[5:])
            if string[4] == "-":
                number *= -1
            if string.startswith("acc"):
                acc += number
                idx += 1
            elif string.startswith("jmp"):
                idx += number
                if idx > n + 1:
                    end_of_program = True
                    acc = 0
                    idx = 0
                    instruction_indices = []
                if idx == n + 1:
                    end_of_program = True
                    proper_ending = True
            else:  # starts with 'nop'
                idx += 1

            if idx == n:
                end_of_program = True
                proper_ending = True
