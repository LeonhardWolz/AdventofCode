import re

def double(n):
    return n * 2

with open("Day_4/input.txt") as f:
    content = f.read().split("\n")
    card_copies = [1]*len(content)
    for index_l, line in enumerate(content):
        line_tokens = re.split(r":|\|", line)
        winners = re.findall(r"(\d+)", line_tokens[1])
        my_numbers = re.findall(r"(\d+)", line_tokens[2])

        win_count = len(set(winners) & set(my_numbers))

        for i in range(1, win_count+1):
            if index_l+i < len(card_copies):
                card_copies[index_l+i] += 1 * card_copies[index_l]

print(sum(card_copies))