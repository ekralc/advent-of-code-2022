import sys
import re
from scipy.optimize import fsolve

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

a, b = fsolve(lambda x: evaluate("root", x), [-1e15, 1e15])

print(int(a))
