# Part I
def list_has_unique_chars(four_chars: list[str]):
    if (
        four_chars[0] == four_chars[1]
        or four_chars[0] == four_chars[2]
        or four_chars[0] == four_chars[3]
    ):
        return False

    if four_chars[1] == four_chars[2] or four_chars[1] == four_chars[3]:
        return False

    if four_chars[2] == four_chars[3]:
        return False

    return True


def start_of_packet(input_filename: str) -> int:
    with open(input_filename, "r") as f:

        for stream in f:
            four_chars = []

            for i, char in enumerate(stream):

                if len(four_chars) == 4:
                    if list_has_unique_chars(four_chars):
                        return i

                    four_chars.pop(0)

                four_chars.append(char)

    return -1


# Part II
def start_of_message(input_filename: str) -> int:
    with open(input_filename, "r") as f:

        for stream in f:
            message_chars = []

            for i, char in enumerate(stream):

                if len(message_chars) == 14:
                    if len(message_chars) == len(set(message_chars)):
                        return i

                    message_chars.pop(0)

                message_chars.append(char)

    return -1


def main():
    # input_filename = "./test_input.txt"
    input_filename = "./input.txt"

    print("Start of Packet:", start_of_packet(input_filename))
    print("Start of Message:", start_of_message(input_filename))


if __name__ == "__main__":
    main()
