from collections import deque
import numpy as np

input = [line.replace('\n', '') for line in  open("aoc_24/input.txt").readlines()]

blizzards = []
start = (0,0)
end = (0,0)
min_coord = (0,0)
max_coord = (len(input[0]) - 2, len(input) - 2)

for ri, r in enumerate(input):
    for ci, c in enumerate(r):
        if ri == 0 and c == ".":
            start = (ci - 1, ri - 1)
        if ri == len(input) - 1 and c == ".":
            end = (ci - 1, ri - 1)

        if c != "#" and c != ".":
           blizzards.append((c, ci - 1, ri -1))

def find_moves(position, end, blizzards, steps, max_coord):
    all_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = position
    possible_moves = []

    for mx,my in all_moves:
        is_possible = True
        np = (x+mx, y+my)
        if np == end: return [np]
        if np[0] < 0 or np[0] >= max_coord[0]: continue
        if np[1] < 0 or np[1] >= max_coord[1]: continue

        for blizzard in blizzards:
            if blizzard[1] != np[0] and blizzard[2] != np[1] and \
                    blizzard[1] != np[0] - 1 and blizzard[2] != np[1] - 1 and \
                    blizzard[1] != np[0] + 1 and blizzard[2] != np[1] + 1:
                        continue

            nbx, nby = blizzard[1], blizzard[2]
            if blizzard[0] == "<":
                nbx = (blizzard[1] - steps) % max_coord[0]
            if blizzard[0] == ">":
                nbx = (blizzard[1] + steps) % max_coord[0]
            if blizzard[0] == "^":
                nby = (blizzard[2] - steps) % max_coord[1]
            if blizzard[0] == "v":
                nby = (blizzard[2] + steps) % max_coord[1]

            if np == (nbx, nby):
                is_possible = False

        if is_possible:
            possible_moves.append(np)

    return possible_moves


cache = {}

def is_possible(np, blizzards, steps, max_coord):
    if np[0] < 0 or np[0] >= max_coord[0]: return False
    if np[1] < 0 or np[1] >= max_coord[1]: return False

    for blizzard in blizzards:
        if blizzard[1] != np[0] and blizzard[2] != np[1] and \
                blizzard[1] != np[0] - 1 and blizzard[2] != np[1] - 1 and \
                blizzard[1] != np[0] + 1 and blizzard[2] != np[1] + 1:
            continue

        nbx, nby = blizzard[1], blizzard[2]
        if blizzard[0] == "<":
            nbx = (blizzard[1] - steps) % max_coord[0]
        if blizzard[0] == ">":
            nbx = (blizzard[1] + steps) % max_coord[0]
        if blizzard[0] == "^":
            nby = (blizzard[2] - steps) % max_coord[1]
        if blizzard[0] == "v":
            nby = (blizzard[2] + steps) % max_coord[1]

        if np == (nbx, nby):
            return False

    return True


def find_path(start, end, blizzards, steps):
    if (steps % 12, start) in cache:
        return cache[(steps % 12, start)]

    if start == end:
        print("End in ", steps)
        print()
        return steps

    moves = []
    while len(moves) == 0 and steps < 70:
        steps += 1
        moves = find_moves(start, end, blizzards, steps, max_coord)

    num_moves = 10000
    for move in moves:
        sub_result = find_path(move, end, blizzards, steps)
        if (steps % 12, move) not in cache:
            cache[(steps % 12, move)] = sub_result
        else:
            cache[(steps % 12, move)] = min(sub_result, cache[(steps % 12, move)])

        num_moves = min(num_moves, sub_result)

    return num_moves


q = deque([(start, 1)])

while True:
    elem, steps = q.pop()

    if elem == end:
        print("End in ", steps)
        print()
        break

    if not is_possible(elem, blizzards, steps, max_coord) and steps != 1:
        continue

    #moves = find_moves(elem, end, blizzards, steps, max_coord)
    direction = [(0,0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    #moves.append(elem)
    for dir in direction:
        move = (elem[0] + dir[0], elem[1] + dir[1])
        ne = (move, (steps + 1) % 600)
        if ne not in cache:
            q.appendleft((move, steps + 1))
            cache[ne] = steps

#total_moves = find_path(start, end, blizzards, 0)

print("Aoc 24.1")


q.clear()
q = deque([(start, 1)])

ends = [end, start, end]
target = 0
cache = {}
initial = True

while True:
    elem, steps = q.pop()
    #if steps % 10 == 0:
    #    print("Length of Queue: ")
    #    print(len(q))
    #    print()

    if elem == ends[target]:
        if target == 2:
            break
        q.clear()
        target += 1
        q.appendleft((elem, steps))
        cache = {}
        initial = True
        continue

    if not is_possible(elem, blizzards, steps, max_coord) and elem != start and elem != end:
        continue

    initial = False

    #moves = find_moves(elem, end, blizzards, steps, max_coord)
    direction = [(0,0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    #moves.append(elem)
    for dir in direction:
        move = (elem[0] + dir[0], elem[1] + dir[1])
        ne = (move, (steps + 1) % 600)
        if ne not in cache:
            q.appendleft((move, steps + 1))
            cache[ne] = steps

print("Aoc 24.2")
print(steps)