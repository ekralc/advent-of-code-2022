import sys

register = 1
count = 0

HEIGHT = 6
WIDTH = 40

grid = [[[] for _ in range(WIDTH)] for _ in range(HEIGHT)]


def draw_pixel():
    column = count % WIDTH
    if abs(register - column) < 2:
        pixel = "#"
    else:
        pixel = " "

    if column == WIDTH - 1:
        pixel += "\n"

    print(pixel, end="")


for line in sys.stdin:
    draw_pixel()
    if line.rstrip().startswith("addx"):
        num = int(line.split()[1])
        count += 1
        draw_pixel()
        register += num

    count += 1
