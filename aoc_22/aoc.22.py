import numpy as np
from functools import reduce

input = [line.replace('\n', '') for line in  open("aoc_22/input.txt").readlines()]

map = input[:-2]
instructions = input[-1]


max_length_line = len(reduce(lambda a, b: a if len(a) > len(b) else b, map))
p_map = np.zeros((len(map), max_length_line))
p_map[:] = -1
def parse_instructions(instructions):
    instr = []

    temp_c = ""

    for i in instructions:
        if i.isnumeric():
            temp_c += i
            continue

        if temp_c != "":
            instr.append(int(temp_c))
            temp_c = ""
        instr.append(i)

    if temp_c != "":
        instr.append(int(temp_c))
    return instr

instructions = parse_instructions(instructions)

start = (0,0)

# -1 void, 0 wall, 1 empty
for r_i, row in enumerate(map):
    for c_i, column in enumerate(row):
        c = -1
        if column == '#':
            c = 0
        if column == '.':
            if r_i == 0 and start == (0,0):
                start = (c_i, r_i)
            c = 1

        p_map[r_i, c_i] = c
# -1 void, 0 wall, 1 empty

def do_step(map, pos, step):
   x,y = pos
   s_x,s_y = step
   return (x + s_x) % len(map[0]), (y + s_y) % len(map)


def move(map, instr, pos, dir):
    if isinstance(instr, str):
        if instr == "R":
            return map, pos, (dir + 1) % 4
        if instr == "L":
            return map, pos, (dir - 1) % 4

    steps = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    step_x, step_y = steps[dir]

    while instr > 0:
        instr -= 1
        nx, ny = do_step(map, pos, (step_x, step_y))
        if map[ny][nx] == 1:
            pos = nx, ny
            continue
        if map[ny][nx] == 0:
            instr = 0
            continue
        while map[ny][nx] == -1:
            nx, ny = do_step(map, (nx, ny), (step_x, step_y))

        if map[ny][nx] == 0:
            instr = 0
            continue

        if map[ny][nx] == 1:
            pos  = nx, ny
            continue
        instr = 0
        continue

    return map, pos, dir

map = p_map
pos = start
dir = 1
for instr in instructions:
    map, pos, dir = move(map, instr, pos, dir)

f_c, f_r = pos
f_c, f_r = f_c + 1, f_r + 1
print("AOC 22.1")
print(1000 * f_r + 4 * f_c + dir - 1)
print("AOC 22.2")
