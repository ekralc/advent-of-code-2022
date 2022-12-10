import sys

stack = [0, 0]

register = 1

count = 1
checkpoints = [20, 60, 100, 140, 180, 220]

total_signal_strength = 0

for line in sys.stdin:
    line = line.rstrip()

    print(count, register)

    if count in checkpoints:
        print(count, register)
        total_signal_strength += count * register
        checkpoints.pop(0)

    if not line.startswith("noop"):
        instruction, arg = line.split()
        arg = int(arg)

        count += 1
        if count in checkpoints:
            total_signal_strength += count * register

        register += arg

    count += 1

print(total_signal_strength)
