import time

input = [inp.replace('\n', '') for inp in open("aoc_15/input.txt").readlines()]
coords = []

for line in input:
    sp = line.split(", ")
    x_s = int(sp[0][len("Sensor at x="):])
    y_s = int(sp[1].split(": ")[0][len("y="):])
    x_b = int(sp[1].split(": ")[1][len("closest beacon is at x="):])
    y_b = int(sp[2][len("y="):])
    coords.append(((x_s, y_s), (x_b, y_b)))

#l= 10
l = 2000000

def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_points_with_radius(rad, center):
    points = []

    for x in range(center[0]-rad, center[0]+rad+1):
        if man_dist(center, (x, l)) <= rad:
            points.append((x, l))

    return points


points_on_l = set({})

all_b = [b for (_, b) in coords]
for (x_s, y_s),(x_b, y_b) in coords:
    dist = man_dist((x_s, y_s), (x_b, y_b))
    for x in range(x_s-dist, x_s+dist+1):
        if man_dist((x_s, y_s), (x, l)) <= dist:
            if (x,l) not in all_b:
                points_on_l.add((x,l))

print(len(points_on_l))
print("AOC 14.1")

def is_covered(p, sensors):
    for s, b, dist in sensors:
        dist_p = man_dist(s, p)
        if dist_p <= dist:
            return True

    return False

min_x = 0
max_x = 4000001
min_y = 0
max_y = 4000001

print("AOC 14.2")
coords = sorted([(s,b, man_dist(s,b)) for s,b in coords], key=lambda x: x[2], reverse=True)
all_sensor_x = sorted([s[0] for s,b,d in coords])

all_points_to_consider = []

for s,b,d in coords:
    points_to_consider = []
    x = (d+1)
    while x > 0:
        if s[0] - x >= 0 and s[1]+(d+1-x) <= max_y:
            nx = s[0] - x
            ny = s[1]+(d+1-x)
            if not is_covered((nx,ny), coords):
                print(nx*4000000+ny)

        if s[0] - x >= 0 and s[1]-(d+1-x) >= 0:
            nx = s[0] - x
            ny = s[1]-(d+1-x)
            if not is_covered((nx,ny), coords):
                print(nx*4000000+ny)

        if s[0] + x <= max_y and s[1]+(d+1-x) <= max_y:
            nx = s[0] + x
            ny = s[1]+(d+1-x)
            if not is_covered((nx,ny), coords):
                print(nx*4000000+ny)

        if s[0] + x <= max_y and s[1]-(d+1-x) >= 0:
            nx = s[0] + x
            ny = s[1]-(d+1-x)
            if not is_covered((nx,ny), coords):
                print(nx*4000000+ny)

        x -= 1

    all_points_to_consider.append(points_to_consider)