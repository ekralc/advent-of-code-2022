import sys

register = 1
count = 0

grid = [[[] for x in range(40)] for x in range(6)]


def draw_pixel():
    row = (count - 1) // 40
    column = count % 40
    output = ""
    if abs(register - column) < 2:
        output = "#"
    else:
        output = " "

    grid[row][column] = output


for line in sys.stdin:
    line = line.rstrip()

    if not line.startswith("noop"):
        instruction, arg = line.split()
        arg = int(arg)

        count += 1
        draw_pixel()

        register += arg

    count += 1
    draw_pixel()

for row in grid:
    for column in row:
        print(column, end="")
    print()
