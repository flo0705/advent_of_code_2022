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

def do_step(pos, step, dir):
   nx, ny = tuple([c+r for c,r in zip(pos, step)])

   cube_length = 50
   max_edge = 4 * cube_length - 1
   # 1
   if ny < 0 and cube_length <= nx < 2 * cube_length and dir == 0:
       nx, ny = 0, nx % cube_length + 3 * cube_length
       dir = (dir + 1) % 4
   elif nx < 0 and 3*cube_length <= ny < 4*cube_length and dir == 3:
       nx, ny = ny % cube_length, 0
       dir = (dir - 1) % 4
   # 4
   elif ny < 0 and 2 * cube_length <= nx < 3 * cube_length and dir == 0:
       nx, ny = nx % cube_length, max_edge
   elif ny > max_edge and 0 <= nx < cube_length and dir == 2:
       nx, ny = nx % cube_length + 2 * cube_length, 0
   # 2
   elif 0 <= nx < cube_length and 0 <= ny < cube_length and dir == 3:
       nx, ny = 0, 49 - ny % cube_length + 2 * cube_length
       dir = (dir + 2) % 4
   elif nx < 0 and 2*cube_length <= ny < 3*cube_length and dir == 3:
       nx, ny = cube_length, 49 - ny % cube_length
       dir = (dir + 2) % 4
   # 3
   elif 0 <= nx < cube_length and cube_length <= ny < 2 * cube_length and dir == 3:
       nx, ny = ny % cube_length, 2 * cube_length
       dir = (dir - 1) % 4
   elif 0 <= nx < cube_length and cube_length <= ny < 2 * cube_length and dir == 0:
       nx, ny = cube_length, nx % cube_length + cube_length
       dir = (dir + 1) % 4
   # 5
   elif nx >= 3*cube_length and 0 <= ny < cube_length and dir == 1:
       nx, ny = 2 * cube_length - 1, (49 - ny % cube_length) + 2 * cube_length
       dir = (dir - 2) % 4
   elif 2*cube_length <= nx < 3*cube_length and 2*cube_length <= ny < 3*cube_length and dir == 1:
       nx, ny = 3*cube_length - 1, 49 - ny % cube_length
       dir = (dir - 2) % 4
   # 6
   elif 2 * cube_length <= nx < 3 * cube_length and cube_length <= ny <= 2*cube_length and dir == 2:
       nx, ny = 2 * cube_length - 1, (nx % cube_length) + cube_length
       dir = (dir + 1) % 4
   elif 2 * cube_length <= nx < 3 * cube_length and cube_length <= ny < 2*cube_length and dir == 1:
       nx, ny = (ny % cube_length) + 2 * cube_length, cube_length - 1
       dir = (dir - 1) % 4
   # 7
   elif cube_length <= nx < 2 * cube_length and 3 * cube_length <= ny < 4 * cube_length and dir == 2:
       nx, ny = cube_length - 1, (nx % cube_length) + 3 * cube_length
       dir = (dir + 1) % 4
   elif cube_length <= nx < 2 * cube_length and 3 * cube_length <= ny < 4 * cube_length and dir == 1:
       nx, ny = (ny % cube_length) + cube_length, 3 * cube_length - 1
       dir = (dir - 1) % 4

   return nx, ny, dir


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

    while instr > 0:
        instr -= 1
        step_x, step_y = steps[dir]
        nx, ny, dir = do_step(pos, (step_x, step_y), dir)
        if map[ny][nx] == 1:
            pos = nx, ny
            print(pos)
            continue
        if map[ny][nx] == 0:
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
print("AOC 22.2")
print(1000 * f_r + 4 * f_c + dir - 1)
