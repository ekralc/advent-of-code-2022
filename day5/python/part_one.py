import sys
import re

from collections import deque

a, instructions = [x for x in sys.stdin.read().split("\n\n")]

stack_lines = a.split("\n")
n = int([x for x in stack_lines[-1] if x.isdigit()][-1])

# Create 'n' stacks
stacks = [deque() for _ in range(n)]

for i, line in enumerate(stack_lines):
    for position, char in enumerate(line):
        if char.isalpha():
            j = position // 4
            stacks[j].append(char)


for instruction in instructions.split("\n"):
    amount, source, destination = [int(x) for x in re.findall(r"\d+", instruction)]

    source -= 1
    destination -= 1

    for _ in range(amount):
        a = stacks[source].popleft()
        stacks[destination].appendleft(a)

final = ""

for stack in stacks:
    final += stack.popleft()

print(final)
