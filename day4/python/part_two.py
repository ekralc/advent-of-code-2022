import sys

count = 0
for line in sys.stdin:
    line = line.rstrip()

    parts = line.split(",")

    a = [int(x) for x in parts[0].split("-")]
    b = [int(x) for x in parts[1].split("-")]

    first = set([i for i in range(a[0], a[1] + 1)])
    second = set([i for i in range(b[0], b[1] + 1)])

    intersection = first.intersection(second)

    if len(intersection) > 0:
        count += 1

print(count)
