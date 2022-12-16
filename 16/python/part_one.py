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



def get_actions(state):
    current_position, _, time_left, _ = state
    actions = []
    if time_left < 1:
        return actions

    if flow[current_position] > 0:
        # Only open valve if it would increase the flow
        actions.append(("open", current_position))

    for neighbour in adj[current_position]:
        actions.append(("move", neighbour))

    return actions

def action(state, action):
    """
    Returns the next state given an action
    """

    current_position, open, time_left, total_flow = state
    command, cave = action

    open = set(open)
    match command:
        case 'open':
            assert cave == current_position
            open.add(cave)
            time_left -= 1
        case 'move':
            assert cave in adj[current_position]
            current_position = cave
            time_left -= 1

    open = frozenset(open)

    total_flow += calculate_flow(open)

    return current_position, open, time_left, total_flow

visited = set()
highest_flow = 0

@functools.cache
def search(state):
    actions = get_actions(state)

    highest_flow = 0
    if len(actions) == 0:
        _, open, _, total_flow = state
        return total_flow - calculate_flow(open)
    for a in actions:
        next_state = action(state, a)
        if identify_state(next_state) not in visited:
            visited.add(identify_state(next_state))
            highest_flow = max(search(next_state), highest_flow)
    
    return highest_flow

@functools.cache
def calculate_flow(open):
    return sum([flow[cave] for cave in open])

def identify_state(state):
    current_position, open, time_left, total_flow = state
    return current_position, open, time_left, total_flow

def show_dist():
    for key, value in dist.items():
        print(key, value)
        print()




initial_state = "AA", frozenset(), 30, 0
print(search(initial_state))