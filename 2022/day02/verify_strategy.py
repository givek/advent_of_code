# Part I

# points_dict = {
#     # Shape Points
#     "X": 1,  # Rock
#     "Y": 2,  # Paper
#     "Z": 3,  # Scissor
#     # ----------------------
#     # Win
#     "AY": 6,  # Rock-Paper
#     "BZ": 6,  # Paper-Scissor
#     "CX": 6,  # Scissor-Rock
#     # ----------------------
#     # Draw
#     "AX": 3,  # Rock-Rock
#     "BY": 3,  # Paper-Paper
#     "CZ": 3,  # Scissor-Scissor
# }
#
#
# def calculate_total_score(input_filename: str):
#     with open(input_filename, "r") as f:
#         total_score = 0
#
#         for moves in f:
#             opp_move, our_move = moves.split()
#
#             # Shape Points
#             total_score += points_dict.get(our_move, 0)
#
#             # Win, Lose OR Draw
#             total_score += points_dict.get(f"{opp_move}{our_move}", 0)
#
#     return total_score


# Part II

shape_points = {
    # Shape Points
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissor
}

outcome_points = {
    # Rock States
    "AX": ("Z", 0),  # Lose = Scissor (Z)
    "AY": ("X", 3),  # Draw = Rock    (X)
    "AZ": ("Y", 6),  # Win  = Paper   (Y)
    # ----------------------
    # Paper States
    "BX": ("X", 0),  # Lose = Rock    (X)
    "BY": ("Y", 3),  # Draw = Paper   (Y)
    "BZ": ("Z", 6),  # Win  = Scissor (Z)
    # ----------------------
    # Scissor States
    "CX": ("Y", 0),  # Lose = Paper   (Y)
    "CY": ("Z", 3),  # Draw = Scissor (Z)
    "CZ": ("X", 6),  # Win  = Rock    (X)
}


def calculate_total_score(input_filename: str):
    with open(input_filename, "r") as f:
        total_score = 0

        for moves in f:
            opp_move, needed_outcome = moves.split()

            needed_shape, score = outcome_points[f"{opp_move}{needed_outcome}"]

            # Win, Lose OR Draw
            total_score += score

            # Shape Points
            total_score += shape_points.get(needed_shape, 0)

    return total_score


def main():
    # input_filename = "./test_input.txt"
    input_filename = "./input.txt"

    print("Total Score: ", calculate_total_score(input_filename))


if __name__ == "__main__":
    main()
