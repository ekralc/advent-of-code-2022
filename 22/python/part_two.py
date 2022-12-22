
import sys
import re

grid = dict()
row_info = dict() # store where each row starts and ends

map, instructions = [a.rstrip() for a in "".join(sys.stdin.readlines()).split("\n\n")]
map = map.splitlines()

for i, line in enumerate(map):
    start = min(line.index("."), line.index("#") if "#" in line else 1000000)
    row_info[i] = (start, len(line))

    for j, char in enumerate(line):
        grid[j, i] = char

pairs = re.findall(r"(\d+)([LR])", instructions)

path = []
for pair in pairs:
    num, rotate = pair
    path.append(int(num))
    path.append(rotate)

facing = 0
current_y = 0
current_x = row_info[0][0]

num_lines = len(row_info.keys())

def get_vertical_boundary(x, y):
    min = 0
    max = num_lines - 1

    for uy in range(y, 0, -1):
        start, end = row_info[uy]
        if x < start or x >= end:
            break

        min = uy

    for dy in range(y, num_lines):
        start, end = row_info[dy]
        if x < start or x >= end:
            break

        max = dy

    return min, max

grid_copy = grid.copy()

print(get_vertical_boundary(3, 5))
def get_char(facing):
    match facing:
        case 0: return ">"
        case 1: return "v"
        case 2: return "<"
        case 3: return "^"

def get_grid_number(x, y):
    column = x // 50
    row = y // 50

    print(column, row)

    return column + row * 3

assert get_grid_number(50, 0) == 1
assert get_grid_number(25, 170) == 9
assert get_grid_number(12, 75) == 3
assert get_grid_number(51, 50) == 4

def get_transition(grid_number, direction):
    transitions = {
        # (1, 0): (2, 0), # right
        # (1, 1): (4, 1), # down
        (1, 2): (6, 0), # left
        (1, 3): (9, 0), # up

        (2, 0): (7, 3),
        (2, 1): (4, 3),
        # (2, 2): (1, 3),
        (2, 3): (9, 3),

        (4, 0): (2, 3),
        # (4, 1): (),
        (4, 2): (6, 1),
        # (4, 3): (),

        # (6, 0): (7, 0),
        # (6, 1): (),
        (6, 2): (1, 0),
        (6, 3): (4, 0),

        (7, 0): (2, 0),
        (7, 1): (9, 0),
        # (7, 2): (),
        # (7, 3): (),

        (9, 0): (7, 3),
        (9, 1): (2, 1),
        (9, 2): (1, 1),
        # (9, 3): ()
    }
    
    return transitions[grid_number, direction]

def get_next_position(x, y, facing):
    start, end = row_info[y]
    min_y, max_y = get_vertical_boundary(x, y)

    assert facing in [0,1,2,3]

    new_x, new_y = x, y
    match facing:
        case 0: # Right
            new_x += 1
            if new_x > end - 1:
                new_x = start

        case 1: # Down
            new_y += 1
            if new_y > max_y:
                new_y = min_y

        case 2: # Left
            new_x -= 1
            if new_x < start:
                new_x = end - 1

        case 3: # Up
            new_y -= 1
            if new_y < min_y:
                new_y = max_y

    return new_x, new_y, facing

def show_grid(grid):
    for y in range(200):
        for x in range(200):
            if (x,y) in grid:
                print(grid[x,y], end="")
            else:
                print(" ", end="")
        print()

for instruction in path:
    if isinstance(instruction, str):
        match instruction:
            case "R": # clockwise
                facing = (facing + 1) % 4
                print("turning clockwise")
            case "L": # anti-clockwise
                facing = (facing - 1) % 4
                print("turning anticlockwise")

    elif isinstance(instruction, int):
        start, length = row_info[current_y]

        new_x, new_y = current_x, current_y
        for x in range(instruction):
            new_x, new_y, facing = get_next_position(new_x, new_y, facing)
            if grid[new_x, new_y] == "#":
                print("breaking, final position: ", current_x, current_y)
                break
            else:
                current_x = new_x
                current_y = new_y
                grid_copy[current_x, current_y] = get_char(facing)

        

print(current_x, current_y, facing)

final_col = current_x + 1
final_row = current_y + 1

print(1000 * final_row + 4 * final_col + facing)