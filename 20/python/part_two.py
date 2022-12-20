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
        if new_idx == 0:
            pairs.append(item)
        elif new_idx == n - 1:
            pairs.insert(0, item)
        else:
            pairs.insert(new_idx, item)

numbers = [num for _, num in pairs]

grove = [1000, 2000, 3000]
sum = 0
for x in grove:
    zero = numbers.index(0)
    idx = (zero + x) % n

    sum += numbers[idx]

print(sum)