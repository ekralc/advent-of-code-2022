import sys

sum = 0
for line in sys.stdin:
    line = line.rstrip()

    mid = len(line) // 2
    compartments = line[:mid], line[mid:]

    set_a, set_b = [set(x) for x in compartments]
    intersection = set_a.intersection(set_b)

    for item in intersection:
        if item.isupper():
            priority = ord(item) - ord("A") + 27
        else:
            priority = ord(item) - ord("a") + 1

        sum += priority

print(sum)
