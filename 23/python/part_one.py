import sys

grid = [list(line.rstrip()) for line in sys.stdin]

directions = ["N", "S", "W", "E"]

m = len(grid)
n = len(grid[1])

def print_grid():
    for y in range(m):
        for x in range(n):
            print(grid[y][x], end="")
        print()

def get_elves():
    elves = set()
    for y in range(m):
        for x in range(n):
            if grid[y][x] == "#":
                elves.add((x, y))

    return elves

def within_bounds(pos):
    x, y = pos
    return x >= 0 and y >=0 and x < n and y < m

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

    return list(filter(within_bounds, adj))

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

    return set(filter(within_bounds, adj))

def positions_are_clear(positions):
    for pos in positions:
        x, y = pos
        if grid[y][x] == "#": return False

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
            print("moving", elf, "to", proposition)
            x, y = elf
            grid[y][x] = "."
            
            x, y = proposition
            grid[y][x] = "#"

    # rotate directions
    directions.append(directions.pop(0))

print_grid()
print()
round()
print_grid()