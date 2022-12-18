import sys
import re

cubes = { tuple(map(int, re.findall("\d+", line))) for line in sys.stdin }

surface_area = 0
for v in cubes:
    open_sides = 6
    x, y, z = v

    for w in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
       if w in cubes:
        open_sides -= 1 

    surface_area += open_sides

print(surface_area)
