input = [inp.replace('\n', '') for inp in open("aoc_14/input.txt").readlines()]

rocks = []
for line in input:
    coords = line.split(" -> ")

    for idx in range(len(coords) - 1):
        [x,y] = coords[idx].split(",")
        [x2,y2] = coords[idx+1].split(",")
        x,y = int(x), int(y)
        x2,y2 = int(x2), int(y2)

        r_x = list(range(min(x, x2), max(x, x2) + 1))
        r_y = list(range(min(y, y2), max(y, y2) + 1))

        if len(r_y) == 1:
            r_y = [r_y[0] for _ in range(len(r_x))]

        if len(r_x) == 1:
            r_x = [r_x[0] for _ in range(len(r_y))]

        rocks += zip(r_x, r_y)

def move(rocks, placed, pos):
    p_x, p_y = pos
    n_pos = (p_x, p_y + 1)
    if n_pos not in rocks and n_pos not in placed:
        return n_pos

    n_pos = (p_x - 1, p_y + 1)
    if n_pos not in rocks and n_pos not in placed:
        return n_pos

    n_pos = (p_x + 1, p_y + 1)
    if n_pos not in rocks and n_pos not in placed:
        return n_pos

    return pos

min_x = min([x for (x, _) in rocks])
max_x = max([x for (x, _) in rocks])
min_y = min([y for (_, y) in rocks])
max_y = max([y for (_, y) in rocks])

placed = []
is_placing = True
while is_placing:
    pos = (500,0)
    while min_x <= pos[0] <= max_x and pos[1] <= max_y:
        is_placing = False
        n_pos = move(rocks, placed, pos)
        if n_pos == pos:
            placed.append(n_pos)
            is_placing = True
            break
        pos = n_pos

print(placed)

for y in range(0, max_y + 1):
    line = ""
    for x in range(min_x, max_x + 1):
        if (x,y) in placed:
            line += "O"
            continue
        if (x, y) in rocks:
            line += "#"
        else:
            line += " "

    print(line)

print("AOC 14.1")
print(len(placed))

placed = []
is_placing = True
path = [(500,0)]
while is_placing:
    pos = path[-1]
    while True:
        is_placing = False
        n_pos = move(rocks, placed, pos)
        path.append(n_pos)
        if n_pos == (500,0):
            placed.append(n_pos)
            path = path[:-1]
            is_placing = False
            break
        if n_pos == pos:
            placed.append(n_pos)
            path = path[:-2]
            is_placing = True
            break

        if n_pos[1] == max_y + 1:
            placed.append(n_pos)
            path = path[:-1]
            is_placing = True
            break
        pos = n_pos

for y in range(0, max_y + 12):
    line = ""
    for x in range(min_x-10, max_x + 10):
        if (x,y) in placed:
            line += "O"
            continue
        if (x, y) in rocks:
            line += "#"
        else:
            line += " "

    print(line)

print(len(placed))

print("AOC 14.2")