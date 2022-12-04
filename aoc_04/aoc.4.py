section_pairs = [[int(section) for section in line.replace("\n", "").replace("-", ",").split(",")]
                 for line in open("aoc_04/input.txt").readlines()]


total = 0
for pair in section_pairs:
    r1 = set(range(pair[0], pair[1] + 1))
    r2 = set(range(pair[2], pair[3] + 1))
    if r1.issubset(r2) or r2.issubset(r1):
        total = total + 1

print("AOC 4.1")
print(total)

total = 0
for pair in section_pairs:
    r1 = set(range(pair[0], pair[1] + 1))
    r2 = set(range(pair[2], pair[3] + 1))
    if len(r1.intersection(r2)) > 0:
        total = total + 1

print("AOC 4.2")
print(total)
