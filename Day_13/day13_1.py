import re

def checkFromRow(pattern, start_row):
    min_dist = len(pattern)-start_row if len(pattern)-start_row < start_row else start_row
    for offset in range(min_dist):
        if(pattern[start_row-1-offset] != pattern[start_row+offset]):
            return False
    
    return True



sum = 0
patterns = []
with open("Day_13/input.txt") as f:
    content = f.read().split("\n\n")
    for block in content:
        pattern = []
        block = block.split("\n")
        for line in block:
            pattern.append(list(line))

        patterns.append(pattern)

for pattern in patterns:
    for row_index in range(1, len(pattern)):
        if(checkFromRow(pattern, row_index)):
            sum += row_index * 100
            break
    
    rotated_pattern = list(zip(*pattern[::-1]))
    for column_index in range(1, len(rotated_pattern)):
        if(checkFromRow(rotated_pattern, column_index)):
            sum += column_index
            break

print(sum)