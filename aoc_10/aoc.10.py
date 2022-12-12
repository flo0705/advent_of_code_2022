input = [inp.replace('\n', '') for inp in open("aoc_10/input.txt").readlines()]

cycle = 1
reg_x = 1
total = 0
cycles = [20, 60, 100, 140, 180, 220]
for cmd in input:
    if "addx" in cmd:
        cycle += 1

        if cycle in cycles:
            total += cycle * reg_x

        reg_x += int(str(cmd[5:]))

    cycle += 1
    if cycle in cycles:
        total += cycle * reg_x

print("AOC 10.1")
print(total)
print("AOC 10.2")

sprite = [0, 1, 2]
lit_pixel = []

reg_x = 1
crt_pos = 0

for cmd in input:
    if crt_pos % 40 in sprite:
        lit_pixel.append(crt_pos)

    if "addx" in cmd:
        crt_pos += 1
        if crt_pos % 40 in sprite:
            lit_pixel.append(crt_pos)

        reg_x += int(str(cmd[5:]))
        sprite = [reg_x - 1, reg_x, reg_x + 1]

    crt_pos += 1

print(lit_pixel)
print(max(lit_pixel))
line = ""
for i in range(0, max(lit_pixel)+6):
    if i in lit_pixel:
        line += "#"
    else:
        line += "."

    if (i+1) % 40 == 0:
        print(line)
        line = ""

print(line)