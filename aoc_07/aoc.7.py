
input = [inp.replace('\n', '') for inp in open("aoc_07/input.txt").readlines()]

filesystem = {}
folder_moves = []

for i in input:
    s = i .split(" ")
    if s[0] == "$":
        if s[1] == "cd":
            if s[2] == "..":
                folder_moves = folder_moves[:-1]
                continue
            folder_moves.append(s[2])
            filesystem["-".join(folder_moves)] = []

        continue

    if s[0] == "dir":
        filesystem["-".join(folder_moves)].append((0, "-".join(folder_moves) + "-" + s[1]))
        continue

    filesystem["-".join(folder_moves)].append((int(s[0]),s[1]))

def calc_size_of_directory(filesystem, dir, directories):
    elems = filesystem[dir]
    size = sum([size if size != 0 else calc_size_of_directory(filesystem, elem, dir_sizes) for (size, elem) in elems])
    directories.append((dir, size))
    return size

dir_sizes = []
calc_size_of_directory(filesystem, "/", dir_sizes)

print("AOC 7.1")
print(sum([size for (_, size) in dir_sizes if size <= 100000]))

total_space = 70000000
to_free_space = 30000000
used_space = dir_sizes[-1][1]
free_space = total_space - used_space
to_free = to_free_space - free_space

print(free_space)

sorted = sorted(dir_sizes, key=lambda y : y[1])
print(sorted)

dir_to_delete = None

for dir_size in sorted:
    if dir_size[1] >= to_free:
        dir_to_delete = dir_size
        break

print(to_free)
print("AOC 7.2")
print(dir_to_delete)