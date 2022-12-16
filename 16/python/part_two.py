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

def show_dist():
    for key, value in dist.items():
        print(key, value)
        print()

# show_dist()


working = { key: value for key, value in adj.items() if flow[key] > 0}

@functools.cache
def dfs(start, time_limit, visited):
    visited = set(visited)

    highest = 0
    for cave in working:
        time_left = time_limit
        if cave in visited: continue

        new_visited = visited.copy()
        new_visited.add(cave)

        time = dist[start][cave]
        if time_left - (time + 1) < 0:
            continue

        # We open the valve at the destination, so add 1
        time_left -= time + 1 
        result = time_left * flow[cave]

        rest = dfs(cave, time_left, frozenset(new_visited))
        result += rest

        highest = max(result, highest)

    return highest

print(dfs("AA", 30, frozenset()))

sys.exit(0)
adj = { key:[a for a in value if a not in open] for key, value in adj.items() if key not in open}
flow = { key:value for key, value in flow.items() if key not in open}
