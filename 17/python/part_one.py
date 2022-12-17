import sys

pattern = list(sys.stdin.readline())
chamber = [['.' for _ in range(7)] for _ in range(1514285714288)]

def display_chamber():
    for row in chamber[::-1]: # reversed
        for char in row:
            print(char, end="")
        print()

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

            if rock[y][x] == "#" and chamber[ny][nx] == "#":
                return False

            if not dry_run:
                if rock[y][x] == "#":
                    chamber[ny][nx] = "#"

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

NUM_ROCKS = 2022
# NUM_ROCKS = 7

rock_idx = 0
max_y = 0
for i in range(1000000000000):
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
    max_y = max(y + h, max_y)
    print("done rock", i)

print(max_y)