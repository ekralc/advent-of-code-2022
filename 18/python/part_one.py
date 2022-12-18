import sys
import re

cubes = set()
for line in sys.stdin:
    cube = tuple([int(a) for a in re.findall("\d+", line.rstrip())])
    cubes.add(cube)

surface_area = 0
for cube in cubes:
    connected_sides = 0

    x, y, z = cube
    for i in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
       if i in cubes:
        connected_sides += 1 

    open_sides = 6 - connected_sides
    surface_area += open_sides

print()
print(surface_area)
