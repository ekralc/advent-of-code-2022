
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
    max = num_lines

    for y in range(y, 0, -1):
        start, end = row_info[y]
        if x < start or x >= end:
            break

        min = y

    for y in range(y, num_lines):
        start, end = row_info[y]
        if x < start or x >= end:
            break

        max = y

    return min, max

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
            min_y, max_y = get_vertical_boundary(new_x, new_y)
            if facing == 0: # right
                new_x = (new_x + 1) % length
                # not wrapping around correctly to start of line
            if facing == 1: # down
                new_y = (new_y + 1) % max_y

            if facing == 2: # left
                new_x = (new_x - 1) % length

            if facing == 3: # up
                new_y = (new_y - 1) % max_y

            if grid[new_x, new_y] == "#":
                print("breaking, final position: ", current_x, current_y)
                break
            else:
                current_x = new_x
                current_y = new_y

        

print(current_x, current_y, facing)

final_col = current_x + 1
final_row = current_y + 1

print(1000 * final_row + 4 * final_col + facing)


