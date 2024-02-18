#Advent of Code 2023: Day 17
from heapq import heappop, heappush
from collections import namedtuple
from icecream import ic

def parse_grid(lines):
    grid = {} #heat_loss on that point
    for r, line in enumerate(lines):
        for c, num in enumerate(line):
            grid[(r,c)] = int(num)
    return grid, r, c

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directions = [(0,1), (1,0), (0,-1), (-1,0)]  # DRUL

#row, column
grid, max_r, max_c = parse_grid(lines)

#total heat loss, row, col, direction, steps
start = [0, 0, 0, 0, 0] #start direction down - may "continue" down or change right

heap = []
heappush(heap, start)
visited = set()

while heap:
    thl, row, col, direction, steps = heappop(heap) #get from heap step with least THL
    for delta_dir in [-1, 0, 1]:  #move left, move forward, move right
        new_direction = (direction + delta_dir) %4
        delta_col, delta_row = directions[new_direction]
        coord = (row + delta_row, col + delta_col)
        if coord == (max_r, max_c):
            result = thl - grid[0,0] + grid[max_r, max_c]
            break
        elif coord in grid.keys():
            new_thl = thl + grid[coord]
            if steps < 3:  # carry on
                r, c = coord
                new_steps = steps + 1 if delta_dir == 0 else 0
                new_state = [new_thl, r, c, new_direction, new_steps]
                if tuple(new_state[1:]) not in visited:
                    visited.add(tuple(new_state[1:]))
                    heappush(heap, new_state)
print(result)