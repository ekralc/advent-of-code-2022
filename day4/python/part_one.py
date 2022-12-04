import sys

count = 0
for line in sys.stdin:
    line = line.rstrip()

    ranges = [[int(x) for x in i.split("-")] for i in line.split(",")]
    a, b = [set([i for i in range(start, finish + 1)]) for (start, finish) in ranges]

    if a.issubset(b) or a.issuperset(b):
        count += 1

print(count)
