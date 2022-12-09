input = [inp.replace('\n', '') for inp in open("aoc_08/input.txt").readlines()]

def is_visible(forest, tree):
    (x,y) = tree
    value = int(forest[y][x])

    if all(int(h) < value for h in forest[y][:x]):
        return True

    if all(int(h) < value for h in forest[y][x+1:]):
        return True

    if all(int(h) < value for h in [h[x] for h in forest[:y]]):
        return True

    if all(int(h) < value for h in [h[x] for h in forest[y+1:]]):
        return True

    return False

def calc_visible_score(forest, tree):
    (x,y) = tree
    value = int(forest[y][x])

    left = reversed([h for h in forest[y][:x]])
    right = [h for h in forest[y][x+1:]]
    up = reversed([h[x] for h in forest[:y]])
    down = [h[x] for h in forest[y+1:]]

    lv = 0
    for l in left:
        lv += 1
        if int(l) >= value:
            break

    rv = 0
    for r in right:
        rv += 1
        if int(r) >= value:
            break
    uv = 0
    for u in up:
        uv += 1
        if int(u) >= value:
            break

    dv = 0
    for d in down:
        dv += 1
        if int(d) >= value:
            break

    return lv * rv * uv * dv

visible_trees = []
for (yi, y) in enumerate(input):
    for xi in range(len(y)):
        if (is_visible(input, (xi, yi))):
            visible_trees.append(y[xi])

print("AOC 8.1")
print(len(visible_trees))

vis_scores = []
for (yi, y) in enumerate(input):
    for xi in range(len(y)):
        if (is_visible(input, (xi, yi))):
            vis_scores.append(((xi, yi), calc_visible_score(input, (xi,yi))))

print("AOC 8.2")
print(sorted(vis_scores, key=lambda k: k[1]))