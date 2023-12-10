import re

def find_diffs(my_lists):
    my_lists = [my_lists]
    main_list = my_lists[len(my_lists)-1]
    diff = []

    if len(main_list) == 1:
        return my_lists + [[0]]

    for index in range(len(main_list)-1):
        diff.append(main_list[index+1]-main_list[index])
    
    if not all(elem == 0 for elem in diff):
        diff = find_diffs(diff)
    
    
    if isinstance(diff[0], int):
        diff = [diff]
    return my_lists + diff

sum = 0
with open("Day_9/input.txt") as f:
    content = f.read().split("\n")
    for sequence in content:
        numbers = list(map(int, re.findall(r"(-*\d+)", sequence)))

        diffs = find_diffs(numbers)
        diffs.reverse()

        new_num = 0
        for entry in diffs:
            new_num = entry[0] - new_num
        sum += new_num

print(sum)