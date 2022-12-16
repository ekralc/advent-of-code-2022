import sys
import time
import os

grid = [[' ' for x in range(1000)] for x in range(1000)]

paths = []
for line in sys.stdin:
   rock_paths = [[int(a) for a in pos.rstrip().split(",")] for pos in line.rstrip().split("->")]
   paths.append(rock_paths)

max_y = -float("inf")

for path in paths:
    for x in range(len(path) - 1):
        a = path[x]
        b = path[x + 1]

        max_y = max([max_y, a[1],  b[1]])

        if a[0] == b[0]:
            # Vertical
            x = a[0]
            start, end = a[1], b[1]
            if start > end:
                swap = start
                start = end
                end = swap
            for y in range(start, end + 1):
                grid[y][x] = "▓" 

        if a[1] == b[1]:
            y = a[1]
            start, end = a[0], b[0]
            if start > end:
                swap = start
                start = end
                end = swap
            for x in range(start, end + 1):
                grid[y][x] = "▓"

line = max_y + 2
for x in range(1000):
    grid[line][x] = "#"

def simulate_sand():
    # Returns the final position of a sand particle, or None if it continuously falls
    initial_pos = (500,0)
    pos = initial_pos
    x, y = pos

    while y < 200:
        below = (x, y + 1)
        x, y = below

        if grid[y][x] == " ":
            pos = below
            continue

        left = (x - 1, y)
        x, y = left
        if grid[y][x] == " ":
            pos = left
            continue

        right = (x + 2, y)
        x, y = right
        if grid[y][x] == " ":
            pos = right
            continue

        # Final position
        return pos

    # falls in to abyss
    if pos[1] == 200:
        return None

    return pos

def draw_screen():
    output = ""
    for y in range(0, line + 1):
        for x in range(400, 600):
            output += grid[y][x]
        output += "\n"

    print(output, end="")

count = 0
while True:
    final_pos = simulate_sand()
    if final_pos == (500, 0):
        break

    count += 1
    x, y = final_pos
    grid[y][x] = "o"

    draw_screen()
    time.sleep(0.1)
    os.system("clear")

print(count + 1)

sys.exit(0)
