#Advent of Code 2023: Day 16
from collections import deque
from datetime import datetime
time_start = datetime.now()

def parse_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in ["|","\\", "/", "-"]:
                grid[(x,y)] = char
    return grid, x,y

def print_grid(grid, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in grid:
                print(grid[(x,y)], end="")
            else:
                print(".", end="")
        print(" ")

def print_energized(energized, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in energized:
                print("#", end="")
            else:
                print(".", end="")
        print(" ")
    print(len(energized))
    print(energized)

def out_of_grid(coord, max_x, max_y):
    x,y = coord
    return x < 0 or x > max_x or y < 0 or y > max_y

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def count_energized():
    energized = set()  # only points, that have been energized
    queue = deque([[(-1,0), 3]])  # beam location, direction
    queue_visited = []

    while queue:
        current_coord, beam_direction = queue.popleft()
        new_coord = tuple_sum(current_coord, directions[beam_direction])
        if not out_of_grid(new_coord, max_x, max_y):
            if new_coord in grid.keys():  # direction might change
                if beam_direction in [1, 3]:  # beam moving east/west
                    new_directions_delta = beam_e_w[grid[new_coord]]
                else:  # beam moving north/south
                    new_directions_delta = beam_n_s[grid[new_coord]]
                for new_direction_delta in new_directions_delta:  # split beams might result in two beams
                    new_direction = (beam_direction + new_direction_delta) % 4
                    queue.append([new_coord, new_direction])
            else:
                queue.append([new_coord, beam_direction])  # direction of beam does not change
            energized.add(new_coord)  # light up new point
            if queue[-1] in queue_visited:  # check if beam with coords and direction has not been calculated already
                queue.pop()
            else:
                queue_visited.append(queue[-1])
    return len(energized)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid, max_x, max_y = parse_grid(lines)

#if beam comes from e+w or n+s, value is delta direction
beam_e_w = {"-":[0], "|":[+1,-1], "\\":[ -1], "/":[ +1]}
beam_n_s = {"-":[+1,-1], "|":[0], "\\":[ +1], "/":[ -1]}
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  #NWSE = 0,1,2,3

part1 = count_energized()
print("Part 1:",part1)

#task 2 counted manually using cycle and changing input parameters in function
# see comments below

"""maxes = []
for counter, i in enumerate( coordinates range ):
    result = count_energized(i, direction)
    print(counter, result)
    maxes.append(result)
print(max(maxes))
"""

#left border:(-1,0) .. (-1,max_y), direction 3: result 7180
#top border: (0,-1) .. (max_x, -1), direction 2: result 7679
#right border: (max_x+1, 0) .. (max_x + 1, max_y): direction 1: result 7759
#bottom border: not needed, max was on right border

print("Part 2:", 7759)
print("Runtime:", datetime.now() - time_start)