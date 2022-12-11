import sys
import re

NUM_ROUNDS = 20


def calculate_operation(op, old):
    rhs = op.split("=")[1].strip()
    return eval(rhs)


monkey_lines = [
    [x.strip() for x in monkey.strip().split("\n")]
    for monkey in sys.stdin.read().split("\n\n")
]

monkeys = [[] for _ in range(len(monkey_lines))]

mod = 1

for num, x in enumerate(monkey_lines):
    monkeys[num] = dict()
    monkeys[num]["inspected"] = 0

    monkeys[num]["items"] = [int(x) for x in re.findall(r"\d+", x[1])]

    operation = x[2].split(":")[1].strip()
    monkeys[num]["operation"] = operation

    test = x[3].split(":")[1].strip()
    test_divisible = int(re.findall(r"\d+", test)[0])
    monkeys[num]["test_divisible"] = test_divisible

    mod *= test_divisible

    monkeys[num]["next_true"] = int(re.findall(r"\d+", x[4])[0])
    monkeys[num]["next_false"] = int(re.findall(r"\d+", x[5])[0])


for _ in range(NUM_ROUNDS):
    for monkey in monkeys:
        num_items = len(monkey["items"])
        for _ in range(num_items):
            worry = int(monkey["items"].pop(0))
            new_worry = calculate_operation(monkey["operation"], worry) // 3

            test_divisible = monkey["test_divisible"]

            if (new_worry % test_divisible) == 0:
                next = monkey["next_true"]
                monkeys[next]["items"].append(new_worry)
            else:
                next = monkey["next_false"]
                monkeys[next]["items"].append(new_worry)

            monkey["inspected"] += 1


inspected = [monkey["inspected"] for monkey in monkeys]
inspected.sort(reverse=True)
print(inspected[0] * inspected[1])
