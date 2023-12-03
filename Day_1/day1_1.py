import re

sum = 0
with open("Day_1/input.txt") as f:
    for line in f:
        line = re.sub(r"\D", r"", line)
        sum += int(line[0] + line[-1])

print(sum)