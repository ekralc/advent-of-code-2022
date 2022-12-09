import sys


NUM_KNOTS = 10
knots = [[0, 0]] * NUM_KNOTS


def move_end(knot, direction, amount=1):
    if direction == "R":
        knot[0] += amount
    elif direction == "L":
        knot[0] -= amount
    elif direction == "U":
        knot[1] += amount
    elif direction == "D":
        knot[1] -= amount

    return knot


def touching(a, b):
    return abs(a[1] - b[1]) <= 1 and abs(a[0] - b[0]) <= 1


visited_tail_positions = set()
for line in sys.stdin:
    line = line.rstrip()

    direction, distance = line.split(" ")
    distance = int(distance)

    print(direction, distance)
    for _ in range(distance):
        knots[0] = move_end(knots[0], direction)

        for x in range(1, NUM_KNOTS):
            if not touching(knots[x - 1], knots[x]):
                knots[x] = move_end(knots[x], direction)

        tail_pos = (knots[-1][0], knots[-1][1])
        visited_tail_positions.add(tail_pos)

print(len(visited_tail_positions))
