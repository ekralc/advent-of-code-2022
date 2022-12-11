import sys
import re

monkeys = dict()

NUM_ROUNDS = 20


def calculate_operation(op, old):
    if "*" in op:
        lhs, rhs = [x.strip() for x in op.split("*")]
        if rhs == "old":
            return old * old
        else:
            return old * int(rhs)
    else:
        lhs, rhs = [x.strip() for x in op.split("+")]
        if rhs == "old":
            return old + old
        else:
            return old + int(rhs)


monkey_lines = [
    [x.strip() for x in monkey.strip().split("\n")]
    for monkey in sys.stdin.read().split("\n\n")
]

num_monkeys = len(monkey_lines)

for x in monkey_lines:
    num = int(re.findall(r"\d+", x[0])[0])
    monkeys[num] = dict()

    items = [int(x) for x in re.findall(r"\d+", x[1])]
    monkeys[num]["items"] = items

    operation = x[2].split(":")[1].strip()
    monkeys[num]["operation"] = operation

    test = x[3].split(":")[1].strip()
    test_divisible = int(re.findall(r"\d+", test)[0])
    monkeys[num]["test_divisible"] = test_divisible

    monkeys[num]["next_true"] = int(re.findall(r"\d+", x[4])[0])
    monkeys[num]["next_false"] = int(re.findall(r"\d+", x[5])[0])

    monkeys[num]["inspected"] = 0

for monkey in monkeys.values():
    print(monkey)

for round in range(NUM_ROUNDS):
    for x in range(num_monkeys):
        print("\n\nMonkey", x)

        monkey = monkeys[x]

        num_items = len(monkey["items"])
        for _ in range(num_items):
            worry = int(monkey["items"].pop(0))
            new_worry = calculate_operation(monkey["operation"], worry)
            new_worry = new_worry // 3

            test_divisible = monkey["test_divisible"]

            if (new_worry % test_divisible) == 0:
                next = monkey["next_true"]
                monkeys[next]["items"].append(new_worry)
            else:
                next = monkey["next_false"]
                monkeys[next]["items"].append(new_worry)

            monkey["inspected"] += 1

        for monkey in monkeys.values():
            print(monkey["items"])

inspected = []
for monkey in monkeys.values():
    inspected.append(monkey["inspected"])

inspected.sort(reverse=True)
print(inspected[0] * inspected[1])
