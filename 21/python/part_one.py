import sys
import re

monkeys = dict()

for line in sys.stdin:
    keys = re.findall("\w{4}", line.rstrip())
    digit = list(map(int, re.findall("\d+", line.rstrip())))
    operator = re.findall("[-+/*]+", line.rstrip())

    key = keys[0]
    monkeys[key] = keys, digit, operator

def evaluate(key):
    print(key)
    monkey = monkeys[key]
    keys, digit, operator = monkey
    if digit:
        return digit[0]
    
    if operator:
        a, b = keys[1:]
        print(operator[0], a, b)
        match operator[0]:
            case '+':
                return evaluate(a) + evaluate(b)
            case '-':
                return evaluate(a) - evaluate(b)
            case '*':
                return evaluate(a) * evaluate(b)
            case '/':
                return evaluate(a) / evaluate(b)

print(evaluate("root"))