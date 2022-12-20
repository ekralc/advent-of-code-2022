import sys

DECRYPTION_KEY = 811589153
numbers = [int(line.rstrip()) * DECRYPTION_KEY for line in sys.stdin]   
n = len(numbers)

# Store the number with its original index for identification
pairs = [(i, num) for i, num in enumerate(numbers)]
queue = pairs[:]

for _ in range(10):
    q = queue[:]
    while q:
        item = q.pop(0)
        i, num = item 

        if num == 0: continue
        idx = pairs.index(item)
        new_idx = (idx + num) % (n - 1)

        del pairs[idx]
        pairs.insert(new_idx, item)

numbers = [num for _, num in pairs]
zero = numbers.index(0)
print(sum(numbers[(zero + x) % n] for x in [1000, 2000, 3000]))