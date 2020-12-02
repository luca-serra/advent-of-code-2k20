INPUT_FILE = "../../data/day_1.txt"

if __name__ == "__main__":

    input_list = [int(integer) for integer in open(INPUT_FILE).readlines()]

    # PART 1

    print("#======= Part 1 =======#")

    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if input_list[i] + input_list[j] == 2020:
                print(f"The two numbers are: {input_list[i]} and {input_list[j]}")
                print(f"Their product is: {input_list[i] * input_list[j]}\n")
                break

    # PART 2

    print("#======= Part 2 =======#")

    for i in range(len(input_list) - 2):
        for j in range(i + 1, len(input_list) - 1):
            for k in range(j + 1, len(input_list)):
                if input_list[i] + input_list[j] + input_list[k] == 2020:
                    print(
                        f"The three numbers are: {input_list[i]}, {input_list[j]} and {input_list[k]}"
                    )
                    print(f"Their product is: {input_list[i] * input_list[j] * input_list[k]}\n")
                    break
