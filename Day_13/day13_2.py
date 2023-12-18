import re

def checkFromRow(pattern, start_row):
    diff_found = False

    min_dist = len(pattern)-start_row if len(pattern)-start_row < start_row else start_row
    for offset in range(min_dist):
        diff = sum(1 for i, j in zip(pattern[start_row-1-offset], pattern[start_row+offset]) if i != j)
        #print(min_dist, diff, diff_found, pattern[start_row-1-offset], pattern[start_row+offset])
        if(diff > 1 or diff == 1 and diff_found):
            return False
        elif(diff == 1 and not diff_found):
            diff_found = True
    
    if diff_found:
        return True
    else:
        return False



total_sum = 0
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
    mirror_found = False

    for row_index in range(1, len(pattern)):
        if(checkFromRow(pattern, row_index)):
            mirror_found = True
            total_sum += row_index * 100
            break
    
    if(not mirror_found):
        rotated_pattern = list(zip(*pattern[::-1]))
        for column_index in range(1, len(rotated_pattern)):
            if(checkFromRow(rotated_pattern, column_index)):
                total_sum += column_index
                break

print(total_sum)