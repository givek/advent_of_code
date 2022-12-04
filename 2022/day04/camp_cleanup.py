# Part I
def total_overlap_pairs(input_filename: str) -> int:

    with open(input_filename, "r") as f:
        overlap_pairs_count = 0

        for pair in f:

            range_one, range_two = pair.split(",")

            range_one_start, range_one_end = map(int, range_one.split("-"))
            range_two_start, range_two_end = map(int, range_two.split("-"))

            if range_one_start <= range_two_start and range_one_end >= range_two_end:
                overlap_pairs_count += 1

            elif range_two_start <= range_one_start and range_two_end >= range_one_end:
                overlap_pairs_count += 1

    return overlap_pairs_count


# Part II
def overlap_pairs(input_filename: str) -> int:

    with open(input_filename, "r") as f:
        overlap_pairs_count = 0

        for pair in f:

            range_one, range_two = pair.split(",")

            range_one_start, range_one_end = map(int, range_one.split("-"))
            range_two_start, range_two_end = map(int, range_two.split("-"))

            if range_one_start <= range_two_start and range_one_end >= range_two_start:
                overlap_pairs_count += 1

            elif (
                range_two_start <= range_one_start and range_two_end >= range_one_start
            ):
                overlap_pairs_count += 1

    return overlap_pairs_count


def main():
    # input_filename = "./test_input.txt"
    input_filename = "./input.txt"

    print("Total Overlaping Pairs:", total_overlap_pairs(input_filename))
    print("Overlaping Pairs:", overlap_pairs(input_filename))


if __name__ == "__main__":
    main()
