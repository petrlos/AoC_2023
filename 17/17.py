#Advent of Code 2023: Day 17
from heapq import heappop, heappush
from collections import namedtuple
from icecream import ic
import time

def parse_grid(lines):
    grid = {} #heat_loss on that point
    for r, line in enumerate(lines):
        for c, num in enumerate(line):
            grid[(r,c)] = int(num)
    return grid, r, c

def find_path(grid):
    Status = namedtuple("Status", ["thl", "row", "col", "dir_index", "steps", "path"])
    # total heat loss, row, col, direction, steps
    start = Status(0, 0, 0, 0, 0, set())  # start direction down - may "continue" down or change right

    heap = []
    heappush(heap, start)
    visited = set()
    results = []

    while heap:
        current = heappop(heap)  # get from heap step with least THL
        for delta_dir in [-1, 0, 1]:  # turn left, carry on, turn right
            new_direction = (delta_dir + current.dir_index) % 4
            delta_row, delta_col = directions[new_direction]
            row = delta_row + current.row  # get new row and col coords
            col = delta_col + current.col
            steps = current.steps + 1 if delta_dir == 0 else 1  # if turn steps = 1, else +1
            path = set()
            path = path | (current.path)
            path.add((row, col))
            if (row, col) in grid.keys():  # inside a grid
                new_status = Status(current.thl + grid[row, col], row, col, new_direction, steps, path)
                checker = new_status[1:-1]
                if steps <= 3 and checker not in visited:
                    visited.add(checker)
                    heappush(heap, new_status)
                if row == max_r and col == max_c:
                    results.append(new_status)
        if len(results) > 2:
            return results

#MAIN - part1 should return 928
with open("test.txt") as file:
    lines = file.read().splitlines()

directions = [(0,1), (1,0), (0,-1), (-1,0)] #RDLU
grid, max_r, max_c = parse_grid(lines)#row, column

result = find_path(grid)
ic(result)