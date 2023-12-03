import re

sum = 0
with open("Day_3/input.txt") as f:
    content = f.read().split("\n")
    for index_l, line in enumerate(content):
        for match_obj in re.finditer(r"(\d+)",line):
            neighbours = ""
            if index_l > 0:
                neighbours += content[index_l-1][max(match_obj.start()-1, 0):min(match_obj.end()+1,len(line))]
            if index_l < len(content)-1:
                neighbours += content[index_l+1][max(match_obj.start()-1, 0):min(match_obj.end()+1,len(line))]
            
            if match_obj.start() > 0:
                neighbours += line[match_obj.start()-1]
            if match_obj.end() < len(line):
                neighbours += line[match_obj.end()]

            if re.search(r"([^\d.])", neighbours):
                sum += int(match_obj.group())


print(sum)

