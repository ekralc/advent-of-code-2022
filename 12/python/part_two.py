import sys

grid = []

start_positions = []
goal_position = ()
for line in sys.stdin:
    line = line.rstrip()

    row = list(line)
    grid.append(row)

    if "E" in row:
        x = row.index("E")
        goal_position = (x, len(grid) - 1)


def climbable(a, b):
    val_a = grid[a[1]][a[0]]
    val_b = grid[b[1]][b[0]]

    if val_a == "S":
        val_a = "a"
    elif val_a == "E":
        val_a = "z"

    if val_b == "S":
        val_b = "a"
    elif val_b == "E":
        val_b = "z"

    difference = ord(val_a) - ord(val_b)
    return difference <= 1


def adjacent(pos):
    """
    Returns an iterator of climbable adjacent candidate squares
    """
    x, y = pos
    candidates = []

    m = len(grid)
    n = len(grid[0])

    if x > 0:
        candidates.append((x - 1, y))
    if x < n - 1:
        candidates.append((x + 1, y))
    if y > 0:
        candidates.append((x, y - 1))
    if y < m - 1:
        candidates.append((x, y + 1))

    return filter(lambda x: climbable(pos, x), candidates)


def bfs(root):
    parent = dict()
    explored = {root}
    queue = [root]

    while len(queue) > 0:
        v = queue.pop(0)

        x, y = v
        if grid[y][x] == "a":
            return v, parent

        for w in adjacent(v):
            if w not in explored:
                parent[w] = v
                explored.add(w)
                queue.append(w)

    return None, parent


def calculate_length(start):
    end, parent = bfs(start)
    if end is None:
        return float("inf")

    backtrace = end
    length = 0
    while backtrace != start:
        backtrace = parent[backtrace]
        length += 1

    return length


print(calculate_length(goal_position))
