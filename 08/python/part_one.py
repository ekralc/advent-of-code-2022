import sys

grid = []
for line in sys.stdin:
    line = line.rstrip()

    row = [int(a) for a in line]
    print(row)

    grid.append(row)

m = len(grid)
n = len(grid[0])

# Set of tuples of coordinates
visible_trees = set()


def is_edge(x, y):
    return y == 0 or y == m - 1 or x == 0 or x == n - 1


# Horizontal
for y in range(m):
    max_height = -1
    # Left to right
    for x in range(n):
        if y == 0 or y == m - 1 or x == 0 or x == n - 1:
            visible_trees.add((x, y))
        if grid[y][x] > max_height:
            visible_trees.add((x, y))
            max_height = grid[y][x]

    max_height = -1
    for x in range(n):
        reversed_row = list(reversed(grid[y]))
        if reversed_row[x] > max_height:
            visible_trees.add((len(grid[0]) - 1 - x, y))
            max_height = reversed_row[x]

# Vertical
for x in range(n):
    max_height = -1
    for y in range(m):
        # Top to bottom
        if is_edge(x, y):
            visible_trees.add((x, y))
        if grid[y][x] > max_height:
            visible_trees.add((x, y))
            print((x, y), "top to bottom")
            max_height = grid[y][x]

    # Bottom to top
    max_height = -1
    reversed_grid = list(reversed(grid))
    for y in range(m):
        if reversed_grid[y][x] > max_height:
            visible_trees.add((x, len(grid) - 1 - y))
            print((x, len(grid) - 1 - y), "bottom to top")
            max_height = reversed_grid[y][x]
            print("new max: ", max_height)

print(visible_trees)
print(len(visible_trees))
