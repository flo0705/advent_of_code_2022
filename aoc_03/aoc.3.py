rucksacks = [line.replace("\n", "") for line in open("aoc_03/input.txt").readlines()]

total = 0
for rucksack in rucksacks:
    comp1 = rucksack[:int(len(rucksack)/2)]
    comp2 = rucksack[int(len(rucksack)/2):]
    intersection = [c1 for c1 in comp1 if c1 in comp2]
    value = ord(intersection[0]) - 64 + 26
    if intersection[0].islower():
        value = ord(intersection[0]) - 96
    total = total + value

print("AOC 3.1")
print(total)

total = 0
groups = [rucksacks[index*3:index * 3 + 3] for index in range(int(len(rucksacks) / 3))]
for group in groups:
    intersection = [g1 for g1 in group[0] if g1 in group[1] and g1 in group[2]]
    value = ord(intersection[0]) - 64 + 26
    if intersection[0].islower():
        value = ord(intersection[0]) - 96

    total = total + value

print("AOC 3.2")
print(total)
