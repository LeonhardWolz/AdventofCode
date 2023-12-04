import re

def double(n):
    return n * 2

sum = 0
with open("Day_4/input.txt") as f:
    content = f.read().split("\n")
    for line in content:
        win_count = 0
        line_tokens = re.split(r":|\|", line)
        winners = re.findall(r"(\d+)", line_tokens[1])
        my_numbers = re.findall(r"(\d+)", line_tokens[2])

        win_count = len(set(winners) & set(my_numbers))
        if(win_count):
            points = 1
            for i in range(win_count-1):
                points = double(points)
            sum += points

print(sum)