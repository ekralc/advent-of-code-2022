import sys
import re

def manhattan(a, b):
    xa, ya = a
    xb, yb = b

    return abs(xa - xb) + abs(ya - yb)

sensors = set()
beacons = set()

sensor_ranges = dict()
for line in sys.stdin:
    sensor, beacon = line.rstrip().split(":")
    sensor_coords = re.findall(r"x=[-+]?\d+, y=[-+]?\d+", sensor.strip())[0]
    sensor_coords = tuple([int(a.split("=")[-1]) for a in sensor_coords.split(", ")])
    beacon_coords = re.findall(r"x=[-+]?\d+, y=[-+]?\d+", beacon.strip())[0]
    beacon_coords = tuple([int(a.split("=")[-1]) for a in beacon_coords.split(", ")])

    sensors.add(sensor_coords)
    beacons.add(beacon_coords)
    
    distance = manhattan(sensor_coords, beacon_coords)

    sensor_ranges[sensor_coords] = distance

def count_vacant_positions(y, start_x, end_x):
    """
    For a given row, count how many positions cannot occupied by a beacon
    """

    occupied = set()
    for x in range(start_x, end_x + 1):
        coord = (x, y)
        if coord in sensors or coord in beacons:
            continue
        for sensor in sensors:
            sensor_max = sensor_ranges[sensor] 

            distance = manhattan(coord, sensor)
            if distance <= sensor_max:
                occupied.add(coord)
                break

    return len(occupied)


min_beacon_x = min(beacon[0] for beacon in beacons)
max_beacon_x = max(beacon[0] for beacon in beacons)
min_sensor_x = min(sensor[0] for sensor in sensors)
max_sensor_x = max(sensor[0] for sensor in sensors)

max_distance = max(distance for distance in sensor_ranges.values())

min_x = min(min_beacon_x, min_sensor_x) - max_distance
max_x = max(max_beacon_x, max_sensor_x) + max_distance

a = count_vacant_positions(2000000, min_x, max_x)
print(a)
            
