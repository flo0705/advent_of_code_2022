import time

input = open("aoc_21/input.txt").readlines()

n_monkeys = {}
o_monkeys = {}

for inp in input:
    inp = inp.replace("\n", "")
    name = inp[:4]

    poss_num = inp.split(": ")[1]
    if poss_num.isnumeric():
        n_monkeys[name] = int(poss_num)
        continue

    dep1 = inp[6:10]
    op = inp[11:12]
    dep2 = inp[13:17]
    o_monkeys[name] = (dep1, dep2, op)

cache = {}
def calc_monkey(monkey):
    if monkey in cache:
        return False, cache[monkey]
    if monkey in n_monkeys:
        if monkey == "humn":
            return True, n_monkeys[monkey]
        return False, n_monkeys[monkey]

    m = o_monkeys[monkey]
    if m[2] == "+":
        is_humn_l, sub_value_l = calc_monkey(m[0])
        is_humn_r, sub_value_r = calc_monkey(m[1])
        if not (is_humn_l or is_humn_r):
            cache[monkey] = sub_value_l + sub_value_r
        return is_humn_r or is_humn_l, sub_value_l + sub_value_r
    if m[2] == "-":
        is_humn_l, sub_value_l = calc_monkey(m[0])
        is_humn_r, sub_value_r = calc_monkey(m[1])
        if not (is_humn_l or is_humn_r):
            cache[monkey] = sub_value_l - sub_value_r
        return is_humn_r or is_humn_l, sub_value_l - sub_value_r
    if m[2] == "*":
        is_humn_l, sub_value_l = calc_monkey(m[0])
        is_humn_r, sub_value_r = calc_monkey(m[1])
        if not (is_humn_l or is_humn_r):
            cache[monkey] = sub_value_l * sub_value_r
        return is_humn_r or is_humn_l, sub_value_l * sub_value_r
    if m[2] == "/":
        is_humn_l, sub_value_l = calc_monkey(m[0])
        is_humn_r, sub_value_r = calc_monkey(m[1])
        if not (is_humn_l or is_humn_r):
            cache[monkey] = sub_value_l / sub_value_r
        return is_humn_r or is_humn_l, sub_value_l / sub_value_r



print("AOC 20.1")
#print(calc_monkey("root"))

print("AOC 20.2")

root = o_monkeys["root"]
_, comp_value = calc_monkey(root[1])

start = time.time()
for i in range(int(33.60561 * pow(10 ,11)), 10 * pow(10,12)):
    n_monkeys["humn"] = i
    _, m_val = calc_monkey(root[0])

    if i % 10000 == 0:
        print("Iteration: ", i)
        print(m_val, comp_value, m_val - comp_value)
    if m_val == comp_value:
        print("HUMN: ", i)
        exit()

print(cache)
print("Took: ", time.time() -start)
