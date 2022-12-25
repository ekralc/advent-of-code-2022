import sys

values = { "2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
reverse = { 2: "2", 1: "1", 0: "0", -1: "-", -2: "=" }

def convert_from(num):
    mult = 1
    sum = 0
    for char in num[::-1]:
        sum += values[char] * mult
        mult *= 5

    return sum

def convert_to(num):
    s = ""
    while num > 0:
        remainder = (num + 2) % 5 - 2
        num = (num - remainder) // 5
        s += reverse[remainder]

    return s[::-1]


numbers = [line.rstrip() for line in sys.stdin]
decimal_total = sum(map(convert_from, numbers))
print(convert_to(decimal_total))
