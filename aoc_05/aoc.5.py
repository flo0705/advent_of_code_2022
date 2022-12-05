stacks, instructions = tuple(open("aoc_05/input.txt").read().split("\n\n"))

instructions = [[int(x) for x in d_instr.split(" ") if x.isnumeric()] for d_instr in instructions.split("\n")]
stacks = [s.replace("[", "").replace("]", "").replace("    "," ").split(" ") for s in stacks.split("\n")[:-1]]

parsed_stack = []

for stack in reversed(stacks):
    if len(parsed_stack) == 0:
        parsed_stack = [[x] for x in stack]
        continue

    for (idx, x) in enumerate(stack):
        if x == '':
            continue
        parsed_stack[idx].append(x)

for instr in instructions:
    parsed_stack[instr[2]-1] = parsed_stack[instr[2]-1] + list(reversed(parsed_stack[instr[1]-1][-instr[0]:]))
    parsed_stack[instr[1]-1] = parsed_stack[instr[1]-1][:-instr[0]]


print("AOC 5.1")
print("".join([top[-1] for top in parsed_stack if len(top) > 0]))

parsed_stack = []
for stack in reversed(stacks):
    if len(parsed_stack) == 0:
        parsed_stack = [[x] for x in stack]
        continue

    for (idx, x) in enumerate(stack):
        if x == '':
            continue
        parsed_stack[idx].append(x)

for instr in instructions:
    parsed_stack[instr[2]-1] = parsed_stack[instr[2]-1] + parsed_stack[instr[1]-1][-instr[0]:]
    parsed_stack[instr[1]-1] = parsed_stack[instr[1]-1][:-instr[0]]

print("AOC 5.2")
print("".join([top[-1] for top in parsed_stack if len(top) > 0]))