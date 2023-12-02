import re


sum = 0
with open("Day_2/input.txt") as f:
    for line in f:
        valid = True
        line = re.split(r":|,|;", line)
        for token in line:
            if re.search(r"red", token):
                print(token)
                count = int(re.sub(r"\D", r"", token))
                if(count > 12):
                    valid = False
            elif re.search(r"green", token):
                count = int(re.sub(r"\D", r"", token))
                if(count > 13):
                    valid = False
            elif re.search(r"blue", token):
                count = int(re.sub(r"\D", r"", token))
                if(count > 14):
                    valid = False
        
        if valid:
            sum += int(re.sub(r"\D", r"", line[0]))

print(sum)