def find_max_calories(input_filename: str):
    with open(input_filename, "r") as f:
        max_calories = 0
        curr_calories = 0

        for calories in f:
            if calories.strip():
                curr_calories += int(calories)
            else:
                max_calories = max(curr_calories, max_calories)
                curr_calories = 0

        max_calories = max(curr_calories, max_calories)

    return max_calories


def find_top_three_max_calories(input_filename: str):
    with open(input_filename, "r") as f:

        third_max_calories = 0
        second_max_calories = 0

        max_calories = 0
        curr_calories = 0

        for calories in f:
            if calories.strip():
                curr_calories += int(calories)
            else:
                if curr_calories > max_calories:
                    third_max_calories = second_max_calories
                    second_max_calories = max_calories
                    max_calories = curr_calories

                elif curr_calories > second_max_calories:
                    third_max_calories = second_max_calories
                    second_max_calories = curr_calories

                elif curr_calories > third_max_calories:
                    third_max_calories = curr_calories

                curr_calories = 0

        if curr_calories > max_calories:
            third_max_calories = second_max_calories
            second_max_calories = max_calories
            max_calories = curr_calories

        elif curr_calories > second_max_calories:
            third_max_calories = second_max_calories
            second_max_calories = curr_calories

        elif curr_calories > third_max_calories:
            third_max_calories = curr_calories

    return max_calories + second_max_calories + third_max_calories


def main():
    # input_filename = "./test_input.txt"
    input_filename = "./input.txt"

    # first half:
    print("Max Calories: ", find_max_calories(input_filename))

    # second half
    print("Top 3 Max Calories: ", find_top_three_max_calories(input_filename))


if __name__ == "__main__":
    main()
