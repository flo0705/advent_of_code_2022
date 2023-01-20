from collections import deque

valves = {}
tunnels = {}

for line in open("aoc_16/input.txt"):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

dists = {}
nonempty = []

print(valves)
print(tunnels)
for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}


def solve(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        time_left = time - dists[valve][neighbor] - 1
        if time_left <= 0:
            continue
        maxval = max(maxval, solve(time_left, neighbor, bitmask | bit) + valves[neighbor] * time_left)

    cache[(time, valve, bitmask)] = maxval
    return maxval


print(solve(30, "AA", 0))
print("AOC 16.1")


b = (1 << len(nonempty)) - 1

m = 0

for i in range((b + 1) // 2):
    m = max(m, solve(26, "AA", i) + solve(26, "AA", b ^ i))

print(m)
print("AOC 16.2")