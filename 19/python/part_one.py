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
def get_max_ore(bp):
    _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = bp
    return max(ore_ore, clay_ore, obs_ore, geo_ore)

@functools.cache
def get_actions(bp, current_state):
    _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = bp

    if current_state.time_left <= 0:
        return {}

    actions = set()
    max_ore = get_max_ore(bp)
    max_clay = obs_clay
    max_obs = geo_obs

    ore = current_state.ore
    clay = current_state.clay
    obsidian = current_state.obsidian

    actions.add("none")
    if ore >= geo_ore and obsidian >= geo_obs:
        return {"build geo"}

    if ore >= obs_ore and clay >= obs_clay and current_state.obsidian_robots < max_obs:
        return {"build obs"}

    if ore >= ore_ore and current_state.ore_robots < max_ore:
        if (ore - current_state.ore_robots) <= ore_ore: # if couldn't afford it before
            actions.add("build ore")

    if ore >= clay_ore and current_state.clay_robots < max_clay:
        if (ore - current_state.ore_robots) <= clay_ore: # if couldn't afford it before
            actions.add("build clay")

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
        # print("ore:", state.ore, "clay:", state.clay, "obs:", state.obsidian, "geodes:", state.geodes)
        assert next_state.time_left >= 0
        max_geodes = max(max_geodes, optimal_geodes(bp, next_state))

    return max_geodes

initial_state = State()

# print(optimal_geodes(blueprints[0], initial_state))

# sys.exit(0)

quality = 0
for i, bp in enumerate(blueprints):
    id = i + 1
    print("Evaluating bp ", id)
    opt = optimal_geodes(bp, State())

    q = opt * id
    print(id, "is complete", opt, q)

    quality += q

print(quality)

