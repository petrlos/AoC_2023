#Advent of Code 2023: Day 10
from collections import deque
def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def parse_pipes(lines):
    maze = dict()
    start = (0,0)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (x,y)
            maze[(x,y)] = char
    return maze, start

def print_pipes(pipes):
    replace_corners = dict(['-─', '|│', 'J┘', 'F┌', 'L└', '7┐', '. '])
    for y in range(5):
        for x in range(5):
            char = pipes[(x,y)]
            if char in replace_corners.keys():
                char = replace_corners[char]
            print(char, end="")
        print(" ")

def count_farthest_point(start, pipes):
    queue = deque([start])
    pipes[start] = "|" #found in data.txt
    distances = {start: 0}
    while queue:
        current = queue.popleft()
        possible_directions = [directions[direction] for direction in pipe_direct_dict[pipes[current]]]
        for possible_direction in possible_directions:
            new_position = tuple_sum(possible_direction, current)
            if new_position not in distances.keys():
                distances[new_position] = distances[current] + 1
                queue.append(new_position)
    return max(distances.values())

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directions = {"N":(0, -1), "S":(0, 1), "W":(-1, 0), "E":(1, 0)}  # UDLR
pipe_direct_dict = dict(zip("|-LJ7F", "NS,EW,NE,NW,SW,SE".split(",")))

pipes, start = parse_pipes(lines)

#Part 1:
print("Part 1:",count_farthest_point(start, pipes))