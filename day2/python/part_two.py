import sys

# X - lose
# Y - draw
# Z - win
outcome_scores = {"X": 0, "Y": 3, "Z": 6}


# A - rock
# B - paper
# C - scissors
shape_scores = {"A": 1, "B": 2, "C": 3}

# Returns the shape to play given an opponent's choice and an expected outcome
def choose_shape(opponent_choice, expected_outcome):
    outcomes = {
        "A": {"X": "C", "Y": "A", "Z": "B"},
        "B": {"X": "A", "Y": "B", "Z": "C"},
        "C": {"X": "B", "Y": "C", "Z": "A"},
    }

    return outcomes[opponent_choice][expected_outcome]


score = 0

for line in sys.stdin:
    line = line.rstrip()
    opponent_choice, expected_outcome = line.split(" ")

    shape = choose_shape(opponent_choice, expected_outcome)

    outcome_score = outcome_scores[expected_outcome]
    shape_score = shape_scores[shape]

    score += outcome_score + shape_score

print(score)
