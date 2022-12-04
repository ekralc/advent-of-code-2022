import sys

count = 0
for line in sys.stdin:
    line = line.rstrip()

    ranges = [[int(x) for x in i.split("-")] for i in line.split(",")]
    a, b = [set([i for i in range(x[0], x[1] + 1)]) for x in ranges]

    intersection = a.intersection(b)

    if intersection == a or intersection == b:
        count += 1

print(count)
