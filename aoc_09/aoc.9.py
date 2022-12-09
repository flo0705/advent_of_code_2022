input = [inp.replace('\n', '').split(" ") for inp in open("aoc_09/input.txt").readlines()]
input = [[inp[0], int(inp[1])] for inp in input]

h = [0,0]
t = [0,0]
route = {tuple(t)}

for (dir, steps) in input:
    for step in range(steps):
        if dir == 'U':
            h[1] += 1
        if dir == 'D':
            h[1] -= 1
        if dir == 'R':
            h[0] += 1
        if dir == 'L':
            h[0] -= 1

        [dx, dy] = [h[i]-t[i] for i in range(len(h))]

        if abs(dx) > 1 or abs(dy) > 1:
            if dx != 0:
                t[0] = t[0] - 1 if dx < 0 else t[0] + 1
            if dy != 0:
                t[1] = t[1] - 1 if dy < 0 else t[1] + 1

        route.add(tuple(t))

print("AOC 9.1")
print(len(route))
knots = [[0,0] for _ in range(10)]
route = {tuple(knots[-1])}

for (dir, steps) in input:
    for step in range(steps):
        if dir == 'U':
            knots[0][1] += 1
        if dir == 'D':
            knots[0][1] -= 1
        if dir == 'R':
            knots[0][0] += 1
        if dir == 'L':
            knots[0][0] -= 1

        for ki, k in enumerate(knots):
            if ki == 0:
                continue

            [dx, dy] = [knots[ki-1][i]-k[i] for i in range(len(k))]
            if abs(dx) > 1 or abs(dy) > 1:
                if dx != 0:
                    knots[ki][0] = knots[ki][0] - 1 if dx < 0 else knots[ki][0] + 1
                if dy != 0:
                    knots[ki][1] = knots[ki][1] - 1 if dy < 0 else knots[ki][1] + 1

        route.add(tuple(knots[-1]))

max_x = max([x for (x,_) in route])
max_y = max([y for (_,y) in route])
min_x = min([x for (x,_) in route])
min_y = min([y for (_,y) in route])

for y in reversed(range(min_y, max_y+1)):
    line = ""
    for x in range(min_x, max_x+1):
        if (x,y) in route:
            line += "X"
        else:
            line += " "
    print(line)

print("AOC 9.2")
print(print(len(route)))