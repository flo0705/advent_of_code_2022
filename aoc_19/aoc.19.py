import time

input = open("aoc_19/input.txt").readlines()


# [(BluePrintNr, OreRobotOre, ClayRobotOre, ObsidianRobotOre, ObsidianRobotClay, GeodeRobotOre, GeodeRobotObsidian)]
templates = []

for temp in input:
    tokens = temp.replace(":", "").split(" ")
    p_template = []
    for t in tokens:
        if t.isnumeric():
            p_template.append(int(t))

    templates.append(p_template)

def get_possible_action(resources, template):
    actions = []

    if resources['ore'] >= template[5] and resources['obsidian'] >= template[6]:
        actions.append("b_geode_r")
        return actions
    if resources['ore'] >= template[1]:
        actions.append("b_ore_r")
    if resources['ore'] >= template[2]:
        actions.append("b_clay_r")
    if resources['ore'] >= template[3] and resources['clay'] >= template[4]:
        actions.append("b_obsidian_r")

    actions.append("noop")

    return actions


cache = {}

def sr(resources):
    return str(resources)

def traverse(template, resources, ore_robots, clay_robots, obs_robots, geode_robots, max_ore, time_left):
    sdr = sr(resources)
    if (sdr, ore_robots, clay_robots, obs_robots, time_left) in cache:
        return cache[(sdr, ore_robots, clay_robots, obs_robots, time_left)]
    if time_left <= 0:
        return resources['geodes']

    if time_left <= 5 and obs_robots < 2:
        return resources['geodes']

    actions = get_possible_action(resources, template)

    num_geodes = 0

    # Update resources:
    resources['ore'] += ore_robots
    resources['clay'] += clay_robots
    resources['obsidian'] += obs_robots
    resources['geodes'] += geode_robots

    if ore_robots >= max_ore:
        actions = [a for a in actions if a != "b_ore_r"]

    if clay_robots >= template[4]:
        actions = [a for a in actions if a != "b_clay_r"]

    if obs_robots >= template[6]:
        actions = [a for a in actions if a != "b_obsidian_r"]

    if ore_robots > 10:
        return resources['geodes']
    if clay_robots > 10:
        return resources['geodes']
    if obs_robots > 10:
        return resources['geodes']

    for action in actions:
        if action == "b_ore_r":
            n_resources = dict(resources)
            n_resources['ore'] -= template[1]
            num_geodes = max(num_geodes, traverse(template, n_resources, ore_robots + 1, clay_robots, obs_robots, geode_robots, max_ore, time_left - 1))
        if action == "b_clay_r":
            n_resources = dict(resources)
            n_resources['ore'] -= template[2]
            num_geodes = max(num_geodes, traverse(template, n_resources, ore_robots, clay_robots + 1, obs_robots, geode_robots, max_ore, time_left - 1))
        if action == "b_obsidian_r":
            n_resources = dict(resources)
            n_resources['ore'] -= template[3]
            n_resources['clay'] -= template[4]
            num_geodes = max(num_geodes, traverse(template, n_resources, ore_robots, clay_robots, obs_robots + 1, geode_robots, max_ore, time_left - 1))
        if action == "b_geode_r":
            n_resources = dict(resources)
            n_resources['ore'] -= template[5]
            n_resources['obsidian'] -= template[6]
            num_geodes = max(num_geodes, traverse(template, n_resources, ore_robots, clay_robots, obs_robots, geode_robots + 1, max_ore, time_left - 1))
        if action == "noop" and len(actions) != 5:
            n_resources = dict(resources)
            num_geodes = max(num_geodes, traverse(template, n_resources, ore_robots, clay_robots, obs_robots, geode_robots, max_ore, time_left - 1))

    cache[(sdr, ore_robots, clay_robots, obs_robots, time_left)] = num_geodes
    return num_geodes


qualities = []

for template in templates[:1]:
    max_ore = max(template[1], template[2], template[3], template[5])
    start = time.time()
    cache = {}
    resources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geodes': 0
    }
    value = traverse(template, resources, 1, 0, 0, 0, max_ore, 24)
    qualities.append(template[0] * value)
    print("Finished template ", template[0])
    print("Value: ", value)
    print("Time: ", time.time() - start)

print("AOC 19.1")
print(sum(qualities))
print("AOC 19.2")

t_value = 1
for template in templates[:3]:
    max_ore = max(template[1], template[2], template[3], template[5])
    start = time.time()
    cache = {}
    resources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geodes': 0
    }
    value = traverse(template, resources, 1, 0, 0, 0, max_ore, 32)
    t_value *= value
    print("Finished template ", template[0])
    print("Value: ", value)
    print("Time: ", time.time() - start)

print(t_value)
