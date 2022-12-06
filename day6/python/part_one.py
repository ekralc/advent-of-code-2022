import sys

buffer = sys.stdin.readline().rstrip()

n = len(buffer)

window_size = 4
chars_processed = 0
for i in range(n - window_size):
    window = buffer[i : i + window_size]
    chars_processed += 1
    if len(set(window)) == window_size:
        break

print(chars_processed + window_size - 1)
