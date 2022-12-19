import sys
import re
import copy
import functools

blueprints = []

for line in sys.stdin:
    blueprint = tuple(map(int, re.findall(r"\d+", line.rstrip())))
    blueprints.append(blueprint)
    
# BFS
class State:
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0

    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0

    time_left = 24

@functools.cache
def get_actions(bp, current_state):
    _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = bp

    if current_state.time_left <= 0:
        return {}

    actions = {"none"}
    if current_state.ore >= ore_ore and (current_state.ore - current_state.ore_robots) < ore_ore:
        actions.add("build ore")

    if current_state.ore >= clay_ore and (current_state.ore - current_state.ore_robots) < clay_ore:
        actions.add("build clay")

    if current_state.ore >= obs_ore and current_state.clay >= obs_clay:
        actions.add("build obs")

    if current_state.ore >= geo_ore and current_state.obsidian >= geo_obs:
        actions.add("build geo")

    return frozenset(actions)

def update_state(bp, current_state, action):
    state = copy.deepcopy(current_state)
    _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = bp

    # Mine 1 resourch for each of its robot types
    state.ore += state.ore_robots
    state.clay += state.clay_robots
    state.obsidian += state.obsidian_robots
    state.geodes += state.geode_robots

    state.time_left -= 1

    match action:
        case "build ore":
            state.ore_robots += 1
            state.ore -= ore_ore
        case "build clay":
            state.clay_robots += 1
            state.ore -= clay_ore
        case "build obs":
            state.obsidian_robots += 1
            state.ore -= obs_ore
            state.clay -= obs_clay
        case "build geo":
            state.geode_robots += 1
            state.ore -= geo_ore
            state.obsidian -= geo_obs

    return state

@functools.cache
def optimal_geodes(bp, state):
    max_geodes = 0

    actions = get_actions(bp, state)
    if len(actions) == 0:
        return state.geodes

    for action in actions:
        next_state = update_state(bp, state, action)
        assert next_state.time_left >= 0
        max_geodes = max(max_geodes, optimal_geodes(bp, next_state))

    return max_geodes

initial_state = State()
print(optimal_geodes(blueprints[1], initial_state))