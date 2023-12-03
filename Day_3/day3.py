import re

sum = 0
with open("Day_3/input.txt") as f:
    content = f.read().split("\n")
    for index_l, line in enumerate(content):
        for match_obj in re.finditer(r"(\*)",line):
            neighbours = []
            if index_l > 0:
                for number_match in re.finditer(r"(\d+)", content[index_l-1]):
                    if match_obj.start()-1 <= number_match.start() <= match_obj.end() or match_obj.start()-1 <= number_match.end()-1 <= match_obj.end():
                        neighbours.append(number_match.group())
                        
            if index_l < len(content)-1:
                for number_match in re.finditer(r"(\d+)", content[index_l+1]):
                    if match_obj.start()-1 <= number_match.start() <= match_obj.end() or match_obj.start()-1 <= number_match.end()-1 <= match_obj.end():
                        neighbours.append(number_match.group())
            
            for number_match in re.finditer(r"(\d+)", line):
                if number_match.end() == match_obj.start() or number_match.start() == match_obj.end():
                    neighbours.append(number_match.group())
            
            if len(neighbours) == 2:
                sum += int(neighbours[0])*int(neighbours[1])

print(sum)

