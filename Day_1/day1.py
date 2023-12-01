import re

digits = {"one" : "1",
          "two" : "2",
          "three" : "3",
          "four" : "4",
          "five" : "5",
          "six" : "6",
          "seven" : "7",
          "eight" : "8",
          "nine" : "9"}

sum = 0
with open("Day_1/input.txt") as f:
    for line in f:
        digit_line = line
        
        for key, value in digits.items():
            for match in re.finditer(key, line):
                lst = list(digit_line)
                lst[match.start()] = value
                    
                digit_line = "".join(lst)
        
        digit_line = re.sub(r"\D", r"", digit_line)
        sum += int(digit_line[0] + digit_line[-1])

print(sum)