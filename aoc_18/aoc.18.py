from collections import deque

input = [tuple([int(i) for i in inp.replace('\n', '').split(",")]) for inp in open("aoc_18/input.txt").readlines()]

def man_dist(a, b):
    return sum([abs(ia-ib) for ia, ib in zip(a,b)])

total_covered = len(input) * 6
for cube in input:
    for cube2 in input:
        if man_dist(cube, cube2) == 1:
            total_covered -= 1

print("AOC 18.1")
print(total_covered)


glob_out = set()
glob_in = set()

def is_out(p, input_list):
    seen = set()
    to_check = deque([p])

    if p in glob_out:
        return True
    if p in glob_in:
        return False

    while len(to_check) > 0:
        n = to_check.popleft()
        if n in input_list or n in seen:
            continue

        seen.add(n)

        if len(seen) > 10000:
            for x in seen:
                glob_out.add(x)
            return True

        for x in [-1,1]:
            to_check.append((n[0]+x, n[1], n[2]))
            to_check.append((n[0], n[1]+x, n[2]))
            to_check.append((n[0], n[1], n[2]+x))

    for x in seen:
        glob_in.add(x)
    return False

total_covered = 0
for x,y,z in input:
    for i in [-1,1]:
        if is_out((x+i,y,z), input):
            total_covered += 1
        if is_out((x,y+i,z), input):
            total_covered += 1
        if is_out((x,y,z+i), input):
            total_covered += 1

print("AOC 18.2")
print(total_covered)