import sys
import re
from scipy.optimize import fsolve
import math

monkeys = dict()

for line in sys.stdin:
    keys = re.findall("\w{4}", line.rstrip())
    digit = list(map(int, re.findall("\d+", line.rstrip())))
    operator = re.findall("[-+/*]+", line.rstrip())

    key = keys[0]
    monkeys[key] = keys, digit, operator

def evaluate(key, humn):
    monkey = monkeys[key]
    keys, digit, operator = monkey

    if key == "root":
        operator = ["-"]

    if key == "humn":
        return humn

    if digit:
        return digit[0]
    
    if operator:
        a, b = keys[1:]
        match operator[0]:
            case '+':
                return evaluate(a, humn) + evaluate(b, humn)
            case '-':
                return evaluate(a, humn) - evaluate(b, humn)
            case '*':
                return evaluate(a, humn) * evaluate(b, humn)
            case '/':
                return evaluate(a, humn) / evaluate(b, humn)

l = -1e15
r = 1e15

while l <= r:
    m = math.floor((l + r) / 2)

    if evaluate("root", m) <= 0:
        l = m + 1
    elif evaluate("root", m) >= 0:
        r = m - 1
    else:
        print("found")
        break

print(l, r, m)

sys.exit(0)

a, b = fsolve(lambda x: evaluate("root", x), [-1e15, 1e15])

print(int(a))
