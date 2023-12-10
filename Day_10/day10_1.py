
grid = []
distance_grids = []

with open("Day_10/input.txt") as f:
    content = f.read().split("\n")
    for line in content:
        grid.append(list(line))


for row_index, row in enumerate(grid):
    for column_index, character in enumerate(row):
        if grid[row_index][column_index] == "S":
            start = (row_index, column_index)

start_connections = []

# Check right side for connection
if start[1]+1 <= len(grid[0]) and grid[start[0]][start[1]+1] in ("J","7", "-"):
    start_connections.append((start[0], start[1]+1))

#Check left side for connection
if start[1]-1 >= 0 and grid[start[0]][start[1]-1] in ("L","F", "-"):
    start_connections.append((start[0], start[1]-1))

#Check top for connection
if start[0]-1 >= 0 and grid[start[0]-1][start[1]] in ("F","7", "|"):
    start_connections.append((start[0]-1, start[1]))

#Check bottom for connection
if start[0]+1 <= len(grid) and grid[start[0]+1][start[1]] in ("L","J", "|"):
    start_connections.append((start[0]+1, start[1]))

for connection in start_connections:
    distance = 1
    distance_grid = [[0 for i in range(len(grid[0]))] for j in grid]
    curr_coordinates = [connection[0], connection[1]]

    while curr_coordinates[0] != start[0] or curr_coordinates[1] != start[1]:
        distance_grid[curr_coordinates[0]][curr_coordinates[1]] = distance

        if grid[curr_coordinates[0]][curr_coordinates[1]] in ("L","F", "-") and curr_coordinates[1]+1 <= len(grid[0]) and (grid[curr_coordinates[0]][curr_coordinates[1]+1] in ("J","7", "-") or (grid[curr_coordinates[0]][curr_coordinates[1]+1] == "S" and distance >= 3)) and distance_grid[curr_coordinates[0]][curr_coordinates[1]+1] == 0:
            curr_coordinates[1] += 1
            
        elif grid[curr_coordinates[0]][curr_coordinates[1]] in ("J","7", "-") and curr_coordinates[1]-1 >= 0 and (grid[curr_coordinates[0]][curr_coordinates[1]-1] in ("L","F", "-") or (grid[curr_coordinates[0]][curr_coordinates[1]-1] == "S" and distance >= 3)) and distance_grid[curr_coordinates[0]][curr_coordinates[1]-1] == 0:
            curr_coordinates[1] -= 1

        elif grid[curr_coordinates[0]][curr_coordinates[1]] in ("F","7", "|") and curr_coordinates[0]+1 <= len(grid) and (grid[curr_coordinates[0]+1][curr_coordinates[1]] in ("L","J", "|") or (grid[curr_coordinates[0]+1][curr_coordinates[1]] == "S" and distance >= 3)) and distance_grid[curr_coordinates[0]+1][curr_coordinates[1]] == 0:
            curr_coordinates[0] += 1

        elif grid[curr_coordinates[0]][curr_coordinates[1]] in ("L","J", "|") and curr_coordinates[0]-1 >= 0 and (grid[curr_coordinates[0]-1][curr_coordinates[1]] in ("F","7", "|") or (grid[curr_coordinates[0]-1][curr_coordinates[1]] == "S" and distance >= 3)) and distance_grid[curr_coordinates[0]-1][curr_coordinates[1]] == 0:
            curr_coordinates[0] -= 1

        else:
            #print("I break:", curr_coordinates)
            break
        distance += 1


    if curr_coordinates[0] == start[0] and curr_coordinates[1] == start[1]:
        distance_grids.append(distance_grid)

fin_distance_grid = [[0 for i in range(len(grid[0]))] for j in grid]
for row_index, row in enumerate(fin_distance_grid):
    for column_index, character in enumerate(row):
        for curr_grid in distance_grids:
            my_distance = curr_grid[row_index][column_index]
            curr_distance = fin_distance_grid[row_index][column_index]
            fin_distance_grid[row_index][column_index] = my_distance if (curr_distance == 0 or my_distance < curr_distance) else curr_distance

print(max([max(elem) for elem in fin_distance_grid]))

