
input = [inp.replace('\n', '') for inp in open("aoc_13/input.txt").readlines()]

def parse_line(line):
    p_line = []
    prevs = []
    curr = p_line
    p_int = ""
    for c in line[1:-1]:
        if c in ["[", "]", ","]:
            if p_int != "":
                curr.append(int(p_int))
                p_int = ""

        if c == "[":
            nl = []
            curr.append(nl)
            prevs.append(curr)
            curr = nl
            continue

        if c == "]":
            curr = prevs[-1]
            prevs = prevs[:-1]
            continue

        if c == ",":
            continue

        p_int += c

    if p_int != "":
        curr.append(int(p_int))
    return p_line

def is_in_order(l1, l2):
    print("comparing:")
    print(l1)
    print(l2)
    print()
    for i in range(max(len(l1), len(l2))):

        if len(l1) <= i:
            print("True")
            return True
        if len(l2) <= i:
            print("False")
            return False

        if isinstance(l1[i], int) and isinstance(l2[i], int):
            if l1[i] < l2[i]:
                print("True")
                return True
            if l1[i] > l2[i]:
                print("False")
                return False

        if isinstance(l1[i], list) and isinstance(l2[i], list):
            temp = is_in_order(l1[i], l2[i])
            if temp is not None:
                return temp

            continue

        if isinstance(l1[i], list) and isinstance(l2[i], int):
            temp = is_in_order(l1[i], [l2[i]])
            if temp is not None:
                return temp

            continue

        if isinstance(l1[i], int) and isinstance(l2[i], list):
            temp = is_in_order([l1[i]], l2[i])

            if temp is not None:
                return temp

            continue

p_input = [parse_line(l) for l in input if l != ""]

indizes = []
for i in range(len(p_input) // 2):
    if is_in_order(p_input[2*i], p_input[2*i+1]):
        indizes.append(i+1)

print("AOC 13.1")
print(sum(indizes))

to_sort = list(p_input)
to_sort.append([[2]])
to_sort.append([[6]])

while True:
    no_change = True
    for i in range(len(to_sort) - 1):
        if not is_in_order(to_sort[i], to_sort[i+1]):
            temp = to_sort[i]
            to_sort[i] = to_sort[i+1]
            to_sort[i+1] = temp
            no_change = False

    if no_change:
        break

print("AOC 13.2")
print((to_sort.index([[2]]) + 1) * (to_sort.index([[6]]) + 1))