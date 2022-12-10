import sys


current_directory = ""
directories = {}


def join_path(base, suffix):
    if base == "/":
        base += suffix
    else:
        base += "/" + suffix

    return base


def calculate_directory_size(dir):
    entry = directories[dir]
    if len(entry["subdirs"]) == 0:
        return entry["size"]

    subdir_sum = 0
    for subdir in entry["subdirs"]:
        subdir_sum += calculate_directory_size(subdir)

    return subdir_sum + entry["size"]


for line in sys.stdin:
    line = line.rstrip()

    if line.startswith("$"):
        cmd = line.split(" ")[1:]

        if cmd[0] == "cd":
            if cmd[1] == "..":
                parts = current_directory.split("/")
                n = len(current_directory) - len(parts[-1]) - 1
                current_directory = current_directory[:n]
                if len(current_directory) == 0:
                    current_directory = "/"

            else:
                if cmd[1] == "/":
                    current_directory = "/"
                else:
                    current_directory = join_path(current_directory, cmd[1])

    else:
        # This is output from 'ls'
        if directories.get(current_directory) == None:
            directories[current_directory] = {"subdirs": [], "size": 0}

        if line.startswith("dir"):
            dir = line.split(" ")[-1]
            path = join_path(current_directory, dir)
            directories[current_directory]["subdirs"].append(path)
        else:  # a file
            size = line.split(" ")[0]
            directories[current_directory]["size"] += int(size)

sum = 0
total_sizes = {}
for key in directories:
    size = calculate_directory_size(key)
    total_sizes[key] = size
    if size <= 100000:
        sum += size

# Calculate the size of the directory to clear
free_space = 70000000 - total_sizes["/"]
space_to_clear = 30000000 - free_space

best_diff = float("inf")
best_size = 0
for key in total_sizes:
    size = total_sizes[key]
    diff = size - space_to_clear

    if diff > 0 and diff < best_diff:
        best_diff = diff
        best_size = size

print(best_size)
