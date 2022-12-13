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


in_order_pairs = set()
for i, pair in enumerate(pairs):
    a, b = pair

    ordered = compare(a,b)
    if compare(a,b):
        in_order_pairs.add(i + 1)

print(sum(in_order_pairs))