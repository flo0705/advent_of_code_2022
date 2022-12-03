inputs = open("aoc_02/input.txt").readlines()

rounds = [input.replace('\n', '').split(" ") for input in inputs]

pf = ["A", "B", "C"]
pr = ["X", "Y", "Z"]

total = 0

for round in rounds:
    if pf.index(round[0]) == pr.index(round[1]):
        total = total + 3 + pr.index(round[1]) + 1

    if pr.index(round[1]) - pf.index(round[0]) == 1:
        total = total + 6 + pr.index(round[1]) + 1

    if pr.index(round[1]) - pf.index(round[0]) == -2:
        total = total + 6 + pr.index(round[1]) + 1

    if pr.index(round[1]) - pf.index(round[0]) == -1:
        total = total + pr.index(round[1]) + 1

    if pr.index(round[1]) - pf.index(round[0]) == 2:
        total = total + pr.index(round[1]) + 1

print("AOC 2.1")
print(total)

total = 0
for round in rounds:
    if  round[1] == "X":
        total = total + (pf.index(round[0]) - 1) % 3 + 1

    if  round[1] == "Y":
        total = total + 3 + pf.index(round[0]) + 1

    if  round[1] == "Z":
        total = total + 6 + (pf.index(round[0]) + 1) % 3 + 1

print("AOC 2.2")
print(total)

#def translate(char):
#    if char == "X":
#        return 0
#
#    if char == "Y":
#        return 3
#
#    if char == "Z":
#        return 6
#
#def round_points(first, response):
#    if  first == response:
#        return 3
#
#    if first == "A" and response == "B":
#        return 6
#
#    if first == "A" and response == "C":
#        return 0
#
#    if first == "B" and response == "A":
#        return 0
#
#    if first == "B" and response == "C":
#        return 6
#
#    if first == "C" and response == "A":
#        return 6
#
#    if first == "C" and response == "B":
#        return 0
#
#def response_points(response):
#    if response == "A":
#        return 1
#
#    if response == "B":
#        return 2
#
#    if response == "C":
#        return 3
#
#def calc_response(first, result_points):
#    if result_points == 3:
#        return first
#
#    if result_points == 6:
#        if first == "A":
#            return "B"
#        if first == "B":
#            return "C"
#        if first == "C":
#            return "A"
#
#    if result_points == 0:
#        if first == "A":
#            return "C"
#        if first == "B":
#            return "A"
#        if first == "C":
#            return "B"
#
#total = 0
#
#for round in rounds:
#    first = round.split(" ")[0]
#    result_points = translate(round.split(" ")[1])
#    response = calc_response(first, result_points)
#
#    total = total + round_points(first, response) + response_points(response)
#
#
#print(total)