file = "aoc_20/input.txt"

input = [(idx, int(x)) for idx, x in enumerate(open(file).readlines())]

places = {(str(idx) + "**" + str(x)): idx for idx, x in input}

def move(key, num, places):
    o_idx = places[key]
    n_idx = (places[key] + num) % (len(input)-1)

    places[key] = n_idx

    for key_1, place in places.items():
        if key == key_1:
            continue

        if n_idx > o_idx and n_idx >= place > o_idx:
            places[key_1] = (place - 1) % len(input)
        if n_idx < o_idx and n_idx <= place < o_idx:
            places[key_1] = (place + 1) % len(input)

    return places

for idx, num in input:
    places = move((str(idx) + "**" + str(num)), num, places)

idx_0 = [idx for key, idx in places.items() if key.endswith("**0")][0]
n_1000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 1000) % (len(input))]
n_2000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 2000) % (len(input))]
n_3000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 3000) % (len(input))]

print("AOC 20.1")
print(sum(n_1000 + n_2000 + n_3000))

multiplier = 811589153

input = [(idx, int(x) * multiplier) for idx, x in enumerate(open(file).readlines())]

places = {(str(idx) + "**" + str(x)): idx for idx, x in input}

def move(key, num, places):
    o_idx = places[key]
    n_idx = (places[key] + num) % (len(input)-1)

    places[key] = n_idx

    for key_1, place in places.items():
        if key == key_1:
            continue

        if n_idx > o_idx and n_idx >= place > o_idx:
            places[key_1] = (place - 1) % len(input)
        if n_idx < o_idx and n_idx <= place < o_idx:
            places[key_1] = (place + 1) % len(input)

    return places

for i in range(10):
    for idx, num in input:
        places = move((str(idx) + "**" + str(num)), num, places)

idx_0 = [idx for key, idx in places.items() if key.endswith("**0")][0]
n_1000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 1000) % (len(input))]
n_2000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 2000) % (len(input))]
n_3000 =  [int(n.split("**")[1]) for n,idx in places.items() if idx == (idx_0 + 3000) % (len(input))]

print("AOC 20.2")
print(sum(n_1000 + n_2000 + n_3000))


print()