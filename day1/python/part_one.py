import sys

elves = 0
calories = [0 for i in range(1000)]

for line in sys.stdin:
    line = line.rstrip()

    if line == "":
        elves += 1
    else:
        calories[elves] += int(line)

calories.sort(reverse=True)

print(calories[0])
