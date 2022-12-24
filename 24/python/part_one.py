import sys
import functools

blizzards = []

m = 0
for y, line in enumerate(sys.stdin):
    m += 1

    line = line.rstrip()
    n = len(line)
    for x, char in enumerate(line):
        if char in [">", "v", "^", "<"]:
            blizzards.append((char, (x, y)))


def update_blizzard(blizzard):
    char, pos = blizzard 
    x, y = pos

    match char:
        case ">":
           x += 1 
        case "<":
            x -= 1
        case "v":
            y += 1
        case "^":
            y -= 1

    if x <= 0: x = n - 2
    if x > (n - 2): x = 1

    if y <= 0: y = m - 2
    if y > (m - 2): y = 1

    return char, (x, y)

def update_all(blizzards):
    return [update_blizzard(a) for a in blizzards]

def get_position_set(blizzards):
    return { pos for _, pos in blizzards }

@functools.cache
def get_position_set_at_time(t):
    new_blizzard = blizzards[:]
    for _ in range(t):
        new_blizzard = update_all(new_blizzard)

    return get_position_set(new_blizzard)

START = (1, 0)
END = (n - 2, m - 1)

def get_actions(state):
    actions = set()

    pos, t = state
    lookahead = get_position_set_at_time(t + 1)
    if pos == START:
        actions.add("none")
        if (1,1) not in lookahead:
            actions.add("down")

    if pos == END:
        actions.add("none")
        if (n - 2, m - 2) not in lookahead:
            actions.add("up")

    if pos == (n - 2, m - 2):
        actions.add("down")

    if pos == (1,1):
        actions.add("up")

    if pos not in lookahead:
        actions.add("none")

    x, y = pos
    if x < n - 2 and y > 0 and y < m - 1:
        if (x + 1, y) not in lookahead:
            actions.add("right")

    if x > 1 and y > 0 and y < m - 1:
        if (x - 1, y) not in lookahead:
            actions.add("left")

    if y < m - 2:
        if (x, y + 1) not in lookahead:
            actions.add("down")

    if y > 1:
        if (x, y - 1) not in lookahead:
            actions.add("up")

    return actions

def get_new_state(state, action):
    pos, t = state
    x, y = pos
    match action:
        case "right": x += 1
        case "left": x -= 1
        case "up": y -= 1
        case "down": y += 1
        
    return (x,y), t + 1

GOAL = END

maximum = 250
visited = set()
def dfs(state):
    pos, t = state

    if pos in get_position_set_at_time(t):
        return float("inf")

    if t >= maximum:
        return float("inf")

    if pos == GOAL:
        return t

    min_t = float("inf")
    actions = get_actions(state)

    for action in actions:
        new_state = get_new_state(state, action)
        if new_state not in visited:
            visited.add(new_state)
            min_t = min(min_t, dfs(new_state))

    return min_t

# Shamefully slow...
# Part 1
first_stage = dfs((START, 0))
print(first_stage)
GOAL = START

maximum = 600
visited = set()
second_stage = dfs((END, first_stage))

maximum = 900
GOAL = END
visited = set()
third_stage = dfs((START, second_stage))

print(third_stage)