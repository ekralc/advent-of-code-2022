from collections import defaultdict
import sys

grid = defaultdict(lambda: ".")

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.rstrip()):
        grid[x,y] = char


directions = ["N", "S", "W", "E"]

round_number = 0
rounds = dict()

def print_grid():
    size = 10
    for y in range(size):
        for x in range(size):
            print(grid[x,y], end = "")
        print()

def get_elves():
    elves = set()
    for pos, value in grid.items():
        if value == "#":
            elves.add(pos)

    return elves

def get_adjacent_cells(elf_pos, direction):
    x, y = elf_pos
    match direction:
        case "N":
            adj = { (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)}           

        case "S":
            adj = { (x - 1, y + 1), (x, y + 1), (x + 1, y + 1) }

        case "W":
            adj = { (x - 1, y - 1), (x - 1, y), (x - 1, y + 1)}

        case "E":
            adj = { (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)}

    return adj

def get_cell_in_direction(elf_pos, direction):
    x, y = elf_pos
    match direction:
        case "N": return (x, y - 1)
        case "S": return (x, y + 1)
        case "E": return(x+1, y)
        case "W": return(x-1, y)

def get_cells_around(elf_pos):
    x, y = elf_pos
    adj = { (x-1,y-1), (x, y-1), (x+1, y-1), (x-1,y), (x+1,y), (x-1,y+1), (x, y+1), (x+1,y+1)}

    return adj

def positions_are_clear(positions):
    for pos in positions:
        if grid[pos] == "#": return False

    return True

def round():
    # first half
    propositions = dict()

    for elf in get_elves():
        around = get_cells_around(elf)
        if positions_are_clear(around): continue # do nothing

        for dir in directions:
            adj = get_adjacent_cells(elf, dir)
            if len(adj) == 0: continue
            if not positions_are_clear(adj): continue

            propositions[elf] = get_cell_in_direction(elf, dir)
            break

    # second half
    for elf, proposition in propositions.items():
        values = list(propositions.values())
        if values.count(proposition) == 1: # unique
            grid[elf] = "."
            grid[proposition] = "#"

    # rotate directions
    directions.append(directions.pop(0))


for i in range(10):
    round()

elves = get_elves()

min_x = min(elf[0] for elf in elves)
max_x = max(elf[0] for elf in elves)

min_y = min(elf[1] for elf in elves)
max_y = max(elf[1] for elf in elves)

count = 0
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if grid[x,y] == ".":
            count += 1

print(count)
