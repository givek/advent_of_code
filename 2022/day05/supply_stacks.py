stack_one = ["T", "R", "G", "W", "Q", "M", "F", "P"]

stack_two = ["R", "F", "H"]

stack_three = ["D", "S", "H", "G", "V", "R", "Z", "P"]

stack_four = ["G", "W", "F", "B", "P", "H", "Q"]

stack_five = ["H", "J", "M", "S", "P"]

stack_six = ["L", "P", "R", "S", "H", "T", "Z", "M"]

stack_seven = ["L", "M", "N", "H", "T", "P"]

stack_eight = ["R", "Q", "D", "F"]

stack_nine = ["H", "P", "L", "N", "C", "S", "D"]


def match_stack(stack_num):
    match stack_num:
        case 1:
            return stack_one
        case 2:
            return stack_two
        case 3:
            return stack_three
        case 4:
            return stack_four
        case 5:
            return stack_five
        case 6:
            return stack_six
        case 7:
            return stack_seven
        case 8:
            return stack_eight
        case 9:
            return stack_nine


# Part I
# def move_from_to(num_crates: int, from_stack, to_stack):
#     while num_crates > 0:
#         try:
#             to_stack.insert(0, from_stack.pop(0))
#             num_crates -= 1
#         except (IndexError):
#             print(to_stack, from_stack)


# Part II
def move_from_to(num_crates: int, from_stack, to_stack):
    while num_crates - 1 >= 0:
        try:
            to_stack.insert(0, from_stack.pop(num_crates - 1))
            num_crates -= 1
        except (IndexError):
            print(to_stack, from_stack)


def rearrage_crates(input_filename: str) -> str:

    with open(input_filename, "r") as f:
        for _ in range(10):
            f.readline()

        for instr in f:

            instr_split = instr.split()

            num_crates = instr_split[1]
            move_from = int(instr_split[3])
            move_to = int(instr_split[5])

            from_stack = match_stack(move_from)

            to_stack = match_stack(move_to)
            # print(from_stack, to_stack)

            move_from_to(int(num_crates), from_stack, to_stack)

    top_crates = ""
    for i in range(1, 10):
        curr_stack = match_stack(i)
        if curr_stack:
            top_crates += curr_stack[0]

    return top_crates


def main():
    input_filename = "./input.txt"

    print(rearrage_crates(input_filename))


if __name__ == "__main__":
    main()
