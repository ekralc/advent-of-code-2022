import functools
import sys
import re
from collections import defaultdict


flow = dict()
adj = dict()

dist = defaultdict(lambda: defaultdict(lambda: float("inf")))

for line in sys.stdin:
    name, flow_rate, *neighbours = re.findall(r"[A-Z]{2}|\d+", line)

    flow[name] = int(flow_rate)
    adj[name] = neighbours

# Floyd-Warshall Algorithm
for cave, neighbours in adj.items():
    for neighbour in neighbours:
        dist[cave][neighbour] = 1
        dist[cave][cave] = 0

for k in adj.keys():
    for i in adj.keys():
        for j in adj.keys():
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Filter out the caves with a rate greater than 0
working = { key: value for key, value in adj.items() if flow[key] > 0}

@functools.cache
def dfs(start_1, start_2, time_limit_1, time_limit_2, visited):
    visited = set(visited)
    highest = 0
    for cave in working:
        if cave in visited: continue

        new_visited = visited.copy()
        new_visited.add(cave)
        # Use frozenset which is hashable
        new_visited = frozenset(new_visited)

        time_1 = dist[start_1][cave]
        if time_limit_1 - time_1 - 1 > 0:
            time_left = time_limit_1 - time_1 - 1 
            move = dfs(cave, start_2, time_left, time_limit_2, new_visited) + (time_left * flow[cave])
            highest = max(move, highest)

        time_2 = dist[start_2][cave]
        if time_limit_2 - time_2 - 1 > 0:
            time_left = time_limit_2 - time_2 - 1
            move = dfs(start_1, cave, time_limit_1, time_left, new_visited) + (time_left * flow[cave])
            highest = max(move, highest)

    return highest

print(dfs("AA", "AA", 26, 26, frozenset()))