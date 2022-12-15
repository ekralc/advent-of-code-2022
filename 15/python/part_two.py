import sys
import re

WINDOW_SIZE = 4000000

def manhattan(a, b):
    xa, ya = a
    xb, yb = b

    return abs(xa - xb) + abs(ya - yb)
    
perimeters = set()
sensor_ranges = dict()
for line in sys.stdin:
    sensor, beacon = line.rstrip().split(":")
    sensor_coords = re.findall(r"x=[-+]?\d+, y=[-+]?\d+", sensor.strip())[0]
    sensor_coords = tuple([int(a.split("=")[-1]) for a in sensor_coords.split(", ")])
    beacon_coords = re.findall(r"x=[-+]?\d+, y=[-+]?\d+", beacon.strip())[0]
    beacon_coords = tuple([int(a.split("=")[-1]) for a in beacon_coords.split(", ")])

    sensor_range = manhattan(sensor_coords, beacon_coords)

    sensor_ranges[sensor_coords] = sensor_range

    start = max(sensor_coords[1] - sensor_range, 0)
    end = min(sensor_coords[1] + sensor_range, WINDOW_SIZE)

    print(start, end)

    for y in range(start, end + 1):
        vertical = abs(y - sensor_coords[1])
        horizontal = sensor_range - vertical + 1
        left, right = ((sensor_coords[0] - horizontal, y), (sensor_coords[0] + horizontal, y))

        if (left[0] >= 0 and left[0] <= WINDOW_SIZE and left[1] >= 0 and left[1] <= WINDOW_SIZE):
            perimeters.add(left)
        if (right[0] >= 0 and right[0] <= WINDOW_SIZE and right[1] >= 0 and right[1] <= WINDOW_SIZE):
            perimeters.add(right)

print(len(perimeters))

# Shameful level of brute force
for coord in perimeters.copy():
    for sensor, range in sensor_ranges.items():
        if manhattan(coord, sensor) <= range:
            if coord in perimeters:
                perimeters.remove(coord)
                print(len(perimeters))
                break

assert len(perimeters) == 1

x, y = perimeters.pop()
print(x * 4000000 + y)
