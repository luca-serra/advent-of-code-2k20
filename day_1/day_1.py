INPUT_FILE = "input.txt"

input_list = [int(integer) for integer in open(INPUT_FILE).readlines()]


# %% PART 1

for i in range(len(input_list) - 1):
    for j in range(i, len(input_list)):
        if input_list[i] + input_list[j] == 2020:
            print(input_list[i], input_list[j])
            print(input_list[i] * input_list[j])
            break

# %% PART 2

for i in range(len(input_list) - 2):
    for j in range(i, len(input_list) - 1):
        for k in range(j, len(input_list)):
            if input_list[i] + input_list[j] + input_list[k] == 2020:
                print(input_list[i], input_list[j], input_list[k])
                print(input_list[i] * input_list[j] * input_list[k])
                break
