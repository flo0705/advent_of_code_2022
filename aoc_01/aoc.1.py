
inputs = open("aoc_01/input.txt").read()
calories = sorted([sum([int(i) for i in input.split('\n')]) for input in inputs.split("\n\n")], reverse=True)

print("AOC 1.1")
print(calories[0])

print("AOC 1.1")
print(sum(calories[:3]))

