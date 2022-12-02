import sys

# A - rock
# B - paper
# C - scissors

# X - rock
# Y - paper
# Z - scissors

shape_scores = {"X": 1, "Y": 2, "Z": 3}

outcomes = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}


score = 0

for line in sys.stdin:
    line = line.rstrip()
    parts = line.split(" ")

    opponent_shape, our_shape = parts

    outcome_score = outcomes[opponent_shape][our_shape]
    shape_score = shape_scores[our_shape]

    score += outcome_score + shape_score

print(score)
