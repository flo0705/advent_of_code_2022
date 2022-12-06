
input = open("aoc_06/input.txt").read()

for i in range(len(input) - 4):
    if len(set(input[i:i+4])) == 4:
        break

print("AOC 6.1")
print(i+4)

for i in range(len(input) - 14):
    if len(set(input[i:i+14])) == 14:
        break

print("AOC 6.2")
print(i+14)
