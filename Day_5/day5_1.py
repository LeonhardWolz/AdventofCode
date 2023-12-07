import re

seeds = []
with open("Day_5/input.txt") as f:
    content = f.read().split("\n\n")
    
    seeds = list(map(int, re.findall(r"(\d+)", content.pop(0))))

    for almanach_map in content:

        mapped = [False for i in range(len(seeds))]
        for line in almanach_map.split(":")[1].split("\n")[1:]:
            ids = list(map(int, re.findall(r"(\d+)", line)))

            for seed_index, seed_id in enumerate(seeds):
                if ids[1] <= seed_id <= ids[1] + ids[2] and not mapped[seed_index]:
                    seeds[seed_index] = ids[0] + (seed_id - ids[1])
                    mapped[seed_index] = True                

print(min(seeds))

        