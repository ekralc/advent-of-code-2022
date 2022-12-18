import sys
import re

sys.setrecursionlimit(10000)

cubes = { tuple(map(int, re.findall("\d+", line))) for line in sys.stdin }

min_coord = tuple(min([x[n] for x in cubes]) - 1 for n in range(3))
max_coord = tuple(max([x[n] for x in cubes]) + 1 for n in range(3))

def within_bounds(pos):
    for x in range(3):
        if pos[x] < min_coord[x] or pos[x] > max_coord[x]:
            return False

    return True

def neighbours(pos):
    x, y, z = pos
    neighbours = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]

    return filter(within_bounds, neighbours)

visited = set()
def dfs(start):
    if start in cubes: return 1

    surface_area = 0
    for pos in neighbours(start):
        if pos not in visited:
            if pos not in cubes:
                visited.add(pos)
            surface_area += dfs(pos)

    return surface_area

print(dfs(min_coord))