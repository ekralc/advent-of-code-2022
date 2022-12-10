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
top_three = calories[0:3]
sum_top_three = sum(top_three)

print(sum_top_three)
