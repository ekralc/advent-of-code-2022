import sys

sum = 0
for line in sys.stdin:
    line = line.rstrip()

    n = len(line) // 2
    a, b = [set(x) for x in [line[:n], line[n:]]]

    intersection = a.intersection(b)

    for item in intersection:
        if item.isupper():
            priority = ord(item) - ord("A") + 27
        else:
            priority = ord(item) - ord("a") + 1

        sum += priority

print(sum)
