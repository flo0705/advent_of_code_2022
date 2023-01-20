import time

directions =  open("aoc_17/input.txt").read().strip()
x_direction = [-1 if x == "<" else 1 for x in directions]


shapes = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(1,0),(1,1),(1,2),(0,1),(2,1)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)]
]

highest_points = [-1 for _ in range(7)]
columns = [[] for _ in range(7)]
def calc_init_position(shape, highest_point, x_directions, i_direction):
    xs = [x for x,y in shape]
    max_x = max(xs)
    min_x = min(xs)

    offset_x = 2
    dirs = x_directions[i_direction:i_direction+3]

    for dir in dirs:
        if max_x + offset_x + dir > 6 or min_x + offset_x + dir < 0:
            continue
        offset_x += dir

    return [(x+offset_x,y+highest_point+1) for x,y in shape]

def check_move_down(shape):
    n_shape = [(x,y-1) for x,y in shape]

    for x,y in n_shape:
        if y in columns[x] or y < 0:
            return False, shape

    return True, n_shape

def check_move_right(shape):
    n_shape = [(x+1,y) for x,y in shape]

    for x, y in n_shape:
        if x > 6 or y in columns[x]:
            return False, shape

    return True, n_shape

def check_move_left(shape):
    n_shape = [(x-1,y) for x,y in shape]

    for x, y in n_shape:
        if x < 0 or y in columns[x]:
            return False, shape

    return True, n_shape


def move(shape, direction):
    if direction < 0:
        moved, shape = check_move_left(shape)
    else:
        moved, shape = check_move_right(shape)

    can_move_down, n_shape = check_move_down(shape)

    if can_move_down:
        return True, n_shape

    return False, n_shape

fallen_rocks = 0
i_dir = 0
reached_end = False

brick = calc_init_position(shapes[fallen_rocks], max(highest_points), x_direction, i_dir)
i_dir += 3
temp_i = -1

def print_(columns):
    for y in range(max(highest_points) + 3, max(highest_points) - 30, -1):
        line = ""
        for x in range(0,7):
            if y in columns[x]:
                line += "X"
            else:
                line += " "
        print(line)

start = time.time()
cache = {}
while fallen_rocks < 1000000000000:

    offset_y = min(highest_points)

    hi = max(highest_points)
    key =  (fallen_rocks % len(shapes), i_dir % len(directions), tuple((h-hi for h in highest_points)))
    if temp_i != fallen_rocks and fallen_rocks != 0: # and fallen_rocks % 1000000 == 0:
        if key in cache:
            cache_rocks, cache_height = cache[key]
            rocks_left = 1000000000000 - fallen_rocks
            n_repetitions = rocks_left // (fallen_rocks - cache_rocks)
            fallen_rocks += n_repetitions * (fallen_rocks - cache_rocks)
            repetition_height_gain = n_repetitions * (max(highest_points) - cache_height)
            cache = {}
            continue
        else:
            cache[key] = (fallen_rocks, max(highest_points))
        temp_i = fallen_rocks

    if reached_end:
        reached_end = False
        brick = calc_init_position(shapes[fallen_rocks % len(shapes)], max(highest_points), x_direction, i_dir % len(x_direction))
        init_brick = brick[:]
        i_dir += 3

    dir = x_direction[i_dir % len(directions)]
    moved, brick = move(brick, dir)

    i_dir += 1
    if moved:
        continue

    offset_y = min(highest_points)
    key = str(shapes[fallen_rocks % len(shapes)]) + str([x - offset_y for x in highest_points])
    cache[key] = max(highest_points)

    for i in range(len(highest_points)):
        if i not in [x for x,y in brick]:
            continue
        n_y = max([y for x,y in brick if x == i])
        n_y = max(highest_points[i], n_y)
        highest_points[i] = n_y

    for x,y in brick:
        columns[x].append(y)
        if len(columns[x]) > 50:
            columns[x] = columns[x][-20:]

    reached_end = True
    fallen_rocks += 1


print("Finished in: ", time.time() - start)
print("AOC 17.1")
print(max(highest_points) + 1)
# 3161
print("AOC 17.2")
print(repetition_height_gain + max(highest_points) + 1)