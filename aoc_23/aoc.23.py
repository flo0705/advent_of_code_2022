import numpy as np

input = [line.replace('\n', '') for line in  open("aoc_23/input.txt").readlines()]

elves = []

for ri, r in enumerate(input):
    for ci, c in enumerate(r):
        if c == '#':
            elves.append((ci, ri))

checks = [
    [(0, -1), (1,-1),(-1,-1)], #N NE NW
    [(0, 1), (1, 1), (-1, 1)], #S SE SW
    [(-1, 0), (-1, -1), (-1, 1)], #W NW SW
    [(1, 0), (1, -1), (1, 1)], #E NE SE
]

flat_checks = [x for c in checks for x in c]
print(flat_checks)

def dist(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - abs(tuple2[1]))

def print_elves(elves):
    x, y = zip(*elves)

    for r in range(min(y), max(y) + 1):
        line = ""
        for c in range(min(x), max(x) + 1):
            if (c, r) in elves:
                line += "#"
            else:
                line += "."

        print(line)

def first_of_n(list, n, start_offset):
    for idx in range(len(list)):
        if list[(idx + start_offset) % len(list)] == n:
            return (idx + start_offset) % len(list)

i = 0
moved = True
while(moved):
    if i % 100 == 0:
        print("Round: ", i)
    # propose
    proposals = []
    duplicates = []
    for elve in elves:
        e_proposal = []
        poss_moves_per_direction = []
        for direction in checks:
            poss_moves_per_direction.append([tuple([x+y for x,y in zip(elve, check)]) for check in direction])

        can_move_direction = [] #N S W E
        for direction in poss_moves_per_direction:
            init = True
            for np in direction:
                if np in elves:
                    init = False
                    break

            can_move_direction.append(init)

        if sum(can_move_direction) == 4 or sum(can_move_direction) == 0:
            continue

        proposed_move = poss_moves_per_direction[first_of_n(can_move_direction, 1, i)][0]
        if proposed_move in [props for _, props in proposals]:
            duplicates.append(proposed_move)
        proposals.append((elve, proposed_move))

    if len(proposals) == 0:
        moved = False

    new_positions = []
    for elve in elves:
        e_proposal = [p for e, p in proposals if e == elve]

        if not e_proposal:
            new_positions.append(elve)
            continue

        e_proposal= e_proposal[0]

        if e_proposal in duplicates:
            new_positions.append(elve)
            continue

        new_positions.append(e_proposal)

    elves = new_positions
    i+=1


    #print()
    #print("Round: ", i + 1)
    #print_elves(elves)
    #print()

x, y = zip(*elves)
empty_fields_count = 0
for r in range(min(y), max(y) + 1):
    for c in range(min(x), max(x) + 1):
        if (c, r) in elves:
            continue

        empty_fields_count += 1

print("AOC 22.1")
print(empty_fields_count)
print("AOC 22.2")
print(i)
