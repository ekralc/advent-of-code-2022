import sys

register = 1
count = 1
total_signal_strength = 0

checkpoints = [20, 60, 100, 140, 180, 220]


for line in sys.stdin:
    if count in checkpoints:
        total_signal_strength += count * register
        checkpoints.pop(0)

    if line.startswith("addx"):
        arg = int(line.rstrip().split()[1])
        count += 1
        if count in checkpoints:
            total_signal_strength += count * register
            checkpoints.pop(0)

        register += arg

    count += 1

print(total_signal_strength)
