import re


sum = 0
with open("Day_2/input.txt") as f:
    for line in f:
        max_red = 0
        max_green = 0
        max_blue = 0

        line = re.split(r":|,|;", line)
        for token in line:
            if re.search(r"red", token):
                print(token)
                count = int(re.sub(r"\D", r"", token))
                max_red = count if count > max_red else max_red

            elif re.search(r"green", token):
                count = int(re.sub(r"\D", r"", token))
                max_green = count if count > max_green else max_green

            elif re.search(r"blue", token):
                count = int(re.sub(r"\D", r"", token))
                max_blue = count if count > max_blue else max_blue
        
        sum += max_red*max_green*max_blue
        

print(sum)