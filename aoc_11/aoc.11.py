input = [[m.strip() for m in monkey.split("\n")] for monkey in open("aoc_11/input.txt").read().split("\n\n")]

monkeys = []

for monkey in input:
    m_nr = int(monkey[0].split(" ")[1][:-1])
    m_items = [int(mon.strip()) for mon in monkey[1].split(":")[1].split(",")]
    m_ops = monkey[2][len("Operation: new = old "):].split(" ")
    m_ops[1] = int(m_ops[1]) if m_ops[1] != "old" else m_ops[1]
    m_test = int(monkey[3][len("Test: divisible by "):])
    m_true = int(monkey[4][len("If true: throw to monkey "):])
    m_false = int(monkey[5][len("If false: throw to monkey "):])
    monkeys.append([m_nr, m_items, m_ops, m_test, m_true, m_false])

sum_inspected = [0 for _ in monkeys]

for rounds in range(20):
    for idx_m, monkey in enumerate(monkeys):
        sum_inspected[idx_m] += len(monkey[1])
        while len(monkey[1]) > 0:
            val = monkey[2][1]
            item = monkey[1][0]
            if val == "old":
                val = item

            if monkey[2][0] == "*":
                monkey[1][0] = (item * val) // 3
            if monkey[2][0] == "+":
                monkey[1][0] = (item + val) // 3

            if monkey[1][0] % monkey[3] == 0:
                monkeys[monkey[4]][1].append(monkey[1][0])
            else:
                monkeys[monkey[5]][1].append(monkey[1][0])

            monkey[1] = monkey[1][1:]


print("AOC 11.1")
sum_inspected = sorted(sum_inspected, reverse=True)[:2]
print(sum_inspected[1] * sum_inspected[0])

monkeys = []

for monkey in input:
    m_nr = int(monkey[0].split(" ")[1][:-1])
    m_items = [int(mon.strip()) for mon in monkey[1].split(":")[1].split(",")]
    m_ops = monkey[2][len("Operation: new = old "):].split(" ")
    m_ops[1] = int(m_ops[1]) if m_ops[1] != "old" else m_ops[1]
    m_test = int(monkey[3][len("Test: divisible by "):])
    m_true = int(monkey[4][len("If true: throw to monkey "):])
    m_false = int(monkey[5][len("If false: throw to monkey "):])
    monkeys.append([m_nr, m_items, m_ops, m_test, m_true, m_false])

sum_inspected = [0 for _ in monkeys]
mod_prod = 1
for x in [monk[3] for monk in monkeys]:
    mod_prod *= x

for rounds in range(10000):
    for idx_m, monkey in enumerate(monkeys):
        sum_inspected[idx_m] += len(monkey[1])
        while len(monkey[1]) > 0:
            val = monkey[2][1]
            item = monkey[1][0]
            if val == "old":
                val = item

            if monkey[2][0] == "*":
                monkey[1][0] = (item * val) % mod_prod
            if monkey[2][0] == "+":
                monkey[1][0] = (item + val) % mod_prod

            if monkey[1][0] % monkey[3] == 0:
                monkeys[monkey[4]][1].append(monkey[1][0])
            else:
                monkeys[monkey[5]][1].append(monkey[1][0])

            monkey[1] = monkey[1][1:]

print("AOC 11.2")
sum_inspected = sorted(sum_inspected, reverse=True)[:2]
print(sum_inspected[1] * sum_inspected[0])
