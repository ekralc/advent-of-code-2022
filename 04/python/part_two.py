import sys

count = 0
for line in sys.stdin:
    line = line.rstrip()

    ranges = [[int(x) for x in i.split("-")] for i in line.split(",")]
    a, b = [set([x for x in range(start, finish + 1)]) for (start, finish) in ranges]

    if not a.isdisjoint(b):
        count += 1

print(count)
