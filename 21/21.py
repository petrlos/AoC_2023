#Advent of Code 2023: Day 21
from collections import deque, defaultdict

def parse_grid(lines):
    start = (0,0)
    grid = defaultdict(lambda: "#") #for part1 - grid has borders
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in ["#", "."]:
                grid[(x, y)] = char
            else:
                grid[(x,y)] = "."
                start = (x,y)
    return grid, start

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def get_plots_visited(grid, start, count): #just bfs
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
    visited = {start: 0}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        neighbours = [tuple_sum(current, direction) for direction in directions]
        for neighbour in neighbours:
            if grid[neighbour] == "." and neighbour not in visited.keys():
                visited[neighbour] = visited[current] + 1
                queue.append(neighbour)
    #only even steps and smaller then count
    return len(list(filter(lambda x: (x %2 == 0) and (x <= count), visited.values())))

#MAIN

with open("data.txt")as file:
    lines = file.read().splitlines()

grid, start = parse_grid(lines)
part1 = get_plots_visited(grid, start, 64)
print("Part 1:", part1)