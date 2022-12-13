import functools
import sys
import ast
current_pair = []

pairs = [[ast.literal_eval(a) for a in x.split("\n")] for x in "".join(sys.stdin.readlines()).split("\n\n")]

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None

        return a < b
    
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if (result := compare(x,y)) is not None:
                return result
        return compare(len(a), len(b))

    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])


def sort_function(a, b):
    output_map = {
        None: 0,
        False: 1,
        True: -1
    }
    return output_map[compare(a,b)]

packets = []
for a, b in pairs:
    packets.append(a)
    packets.append(b)

packets.append([[2]])
packets.append([[6]])

key=functools.cmp_to_key(sort_function)
packets.sort(key=key)

first = packets.index([[2]]) + 1
second = packets.index([[6]]) + 1

print(first * second)

