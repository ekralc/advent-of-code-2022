import sys

grid = []
for line in sys.stdin:
    line = line.rstrip()

    row = [int(a) for a in line]

    grid.append(row)

m = len(grid)
n = len(grid[0])


def is_edge(x, y):
    return y == 0 or y == m - 1 or x == 0 or x == n - 1


highest = -1

for y in range(m):
    for x in range(n):
        height = grid[y][x]
        scenic_score = 0
        if is_edge(x, y):
            continue

        # Right
        right = 0
        for j in range(x + 1, n):
            right += 1
            if grid[y][j] >= height:
                break

        left = 0
        for j in range(x - 1, -1, -1):
            left += 1
            if grid[y][j] >= height:
                break

        # Down
        down = 0
        for j in range(y + 1, m):
            down += 1
            if grid[j][x] >= height:
                break

        # Up
        up = 0
        for j in range(y - 1, -1, -1):
            up += 1
            if grid[j][x] >= height:
                break

        scenic_score = left * right * down * up
        print(x, y, ":", up, left, down, right, "total:", scenic_score)
        highest = max(scenic_score, highest)

print(highest)
