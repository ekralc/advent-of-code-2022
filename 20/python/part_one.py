import sys

numbers = [int(line.rstrip()) for line in sys.stdin]   

n = len(numbers)

pairs = [(i, num) for i, num in enumerate(numbers)]
queue = pairs[:]

for _ in range(n):
    item = queue.pop(0)
    i, num = item 

    if num == 0: continue
    idx = pairs.index(item)
    new_idx = (idx + num) % (n - 1)

    del pairs[idx]
    if new_idx == 0:
        pairs.append(item)
    elif new_idx == n - 1:
        pairs.insert(0, item)
    else:
        pairs.insert(new_idx, item)

numbers = [num for _, num in pairs]
print(numbers)

grove = [1000, 2000, 3000]
sum = 0
for x in grove:
    zero = numbers.index(0)
    idx = (zero + x) % n

    sum += numbers[idx]

print(sum)