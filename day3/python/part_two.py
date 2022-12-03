import sys

bags = []
for line in sys.stdin:
    line = line.rstrip()
    bags.append(line)

n = len(bags)
sum = 0

for i in range(0, n, 3):
    group = bags[i : i + 3]
    a, b, c = [set(x) for x in group]

    intersection = a.intersection(b).intersection(c)
    item = intersection.pop()

    if item.isupper():
        priority = ord(item) - ord("A") + 27
    else:
        priority = ord(item) - ord("a") + 1

    sum += priority

print(sum)
