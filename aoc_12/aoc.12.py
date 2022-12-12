import math

# coordinates = (y,x)
def pos_d(s, input):
    ds = []
    val_x = ord(input[s[0]][s[1]].replace("S", "a"))

    if s[1] < len(input[0]) - 1 and val_x + 1 >= ord(input[s[0]][s[1]+1].replace("E", "z")):
        ds.append((s[0],s[1]+1))

    if s[0] < len(input) - 1 and val_x + 1 >= ord(input[s[0]+1][s[1]].replace("E", "z")):
        ds.append((s[0]+1,s[1]))

    if s[1] != 0 and val_x + 1 >= ord(input[s[0]][s[1]-1].replace("E", "z")):
        ds.append((s[0], s[1]-1))

    if s[0] != 0 and val_x + 1 >= ord(input[s[0]-1][s[1]].replace("E", "z")):
        ds.append((s[0]-1, s[1]))

    return ds

def dijkstra(graqh, start, end):
    routes = [[math.inf for _ in range(len(row))] for row in graqh]
    routes[start[0]][start[1]] = 0
    to_visit = [start]
    while len(to_visit) > 0:
        sy, sx = to_visit[0]
        neighbours = pos_d((sy,sx), graqh)

        for ny, nx in neighbours:
            n_val = routes[sy][sx] + 1
            if routes[ny][nx] < n_val:
                continue

            routes[ny][nx] = n_val
            if (ny,nx) not in to_visit:
                to_visit.append((ny,nx))

        to_visit = to_visit[1:]

    return routes[end[0]][end[1]]

input = [inp.replace('\n', '') for inp in open("aoc_12/input.txt").readlines()]

s = ("".join(input).find("S") // len(input[0]), "".join(input).find("S") % len(input[0]))
e = ("".join(input).find("E") // len(input[0]), "".join(input).find("E") % len(input[0]))


print("AOC 12.1")
print(dijkstra(input, s, e))

aas = [(yi, xi) for (yi, y) in enumerate(input) for (xi, x) in enumerate(y) if x == "a" ]
a_vals = sorted([(dijkstra(input, a, e), a) for a in aas], key=lambda x: x[0])

print("AOC 12.2")
print(a_vals[0])
