import sys
from collections import defaultdict

pattern = list(sys.stdin.readline())
chamber = defaultdict(lambda: '.')
NUM_ROCKS = 100000

def get_direction():
    direction = pattern.pop(0)
    pattern.append(direction)

    match direction:
        case '>':
            return 1
        case '<':
            return -1

def rock_shape(rock):
    return len(rock[0]), len(rock)

def commit_rock(rock, pos, dry_run=False):
    w, h = rock_shape(rock)
    rx, ry = pos

    if ry < 0 or rx >= 7 or rx < 0:
        return False

    if rx + w - 1 >= 7 or ry < 0:
        return False

    for x in range(w):
        for y in range(h):
            nx = rx + x
            ny = ry + y

            if rock[y][x] == "#" and chamber[nx, ny] == "#":
                return False

            if not dry_run:
                if rock[y][x] == "#":
                    chamber[nx, ny] = "#"

    return True


rocks = [
    [["#", "#", "#", "#"]],

    [
        [".", "#", "."],
        ["#", "#", "#"],
        [".", "#", "."]
    ],

    [
        [".", ".", "#"],
        [".", ".", "#"],
        ["#", "#", "#"],
    ],

    [
        ["#"],
        ["#"],
        ["#"],
        ["#"]
    ],

    [
        ["#", "#"],
        ["#", "#"]
    ]
]

rocks = [rock[::-1] for rock in rocks]

max_after_n_rocks = dict()
max_after_n_rocks[-1] = 0

rock_idx = 0
max_y = 0
for i in range(NUM_ROCKS):
    rock = rocks[rock_idx]
    rock_idx = (rock_idx + 1) % len(rocks)

    w, h = rock_shape(rock)
    x, y = (2, max_y + 3)

    while True:
        direction = get_direction()

        new_pos = (x + direction, y) 
        if commit_rock(rock, new_pos, True):
            x, y = new_pos

        new_pos = (x, y - 1)
        if commit_rock(rock, new_pos, True):
            x, y = new_pos
        else:
            break
    
    commit_rock(rock, (x, y), False)
    old_max = max_y
    max_y = max(max_y, y + h)
    top_y = y + h

    max_after_n_rocks[i] = max_y - old_max 

final_string = ""
for key, value in max_after_n_rocks.items():
        final_string += str(value)

# print(final_string)

# From here I manually found the repeating pattern of the string as a shortcut
# (too lazy to write a program for this)

# Manually fill these in
preamble = ""
repeating_pattern = ""

sum_preamble = sum(list(map(int, preamble)))
sum_repeat = sum(list(map(int, repeating_pattern)))

pattern_length = len(repeating_pattern)

total_rocks = 1000000000000
remaining = total_rocks - len(preamble)

num_repeats = remaining // pattern_length
total_sum = sum_preamble + num_repeats * sum_repeat

remainder = (total_rocks - len(preamble)) % num_repeats
total_sum += sum(list(map(int, repeating_pattern))[:remainder + 1])

print(total_sum)