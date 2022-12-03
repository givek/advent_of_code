# Part I
def sum_of_priorities(input_filename: str) -> int:

    with open(input_filename, "r") as f:

        priority_sum = 0

        for contents in f:

            first_compartment_items = set(contents[: len(contents) // 2])

            for item in contents[len(contents) // 2 :]:

                if item in first_compartment_items:

                    if ord(item) <= 90:
                        priority_sum += (ord(item) - 65) + 27
                    else:
                        priority_sum += ord(item) - 96

                    break

    return priority_sum


# Part II
# def sum_of_priorities(input_filename: str) -> int:
#
#     with open(input_filename, "r") as f:
#
#         priority_sum = 0
#
#         first_elf_items = set()
#         second_elf_items = set()
#
#         for i, contents in enumerate(f):
#
#             if i % 3 == 0:
#                 first_elf_items = set(contents)
#
#             elif i % 3 == 1:
#                 second_elf_items = set(contents)
#
#             else:
#
#                 for item in contents:
#
#                     if item in first_elf_items and item in second_elf_items:
#
#                         if ord(item) <= 90:
#                             priority_sum += (ord(item) - 65) + 27
#                         else:
#                             priority_sum += ord(item) - 96
#
#                         first_elf_items = set()
#                         second_elf_items = set()
#
#                         break
#
#     return priority_sum


def main():
    # input_filename = "./test_input.txt"
    input_filename = "./input.txt"

    print("Sum of Priorities is:", sum_of_priorities(input_filename))


if __name__ == "__main__":
    main()
