#Advent of Code 2023: Day 18
from collections import defaultdict, deque, Counter
from datetime import datetime
time_start = datetime.now()

def parse_instructions(lines):
    instructions = []
    for line in lines:
        direction, count, colour = line.split(" ")
        instructions.append([direction, int(count), colour])
    return instructions

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def print_field():
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            print(field[(x,y)], end="")
        print(" ")

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

instructions = parse_instructions(lines)

digged_out = set()
position = (0,0)
directions = {"U":(0, -1), "D":(0, 1), "L":(-1, 0), "R":(1, 0)}  # UDLR

#dig trench
for instruction in instructions:
    direction, count, colour = instruction
    for _ in range(count):
        position = tuple_sum(position, directions[direction])
        digged_out.add(position)

#get total size of field
x_s = [coord[0] for coord in digged_out]
y_s = [coord[1] for coord in digged_out]
max_x, min_x = max(x_s)+2, min(x_s)-1
max_y, min_y = max(y_s)+2, min(y_s)-1

#rewrite set to dictionary - mark each coordinate as digged, everything else is not digged
field = defaultdict(lambda: ".")
for cube in digged_out:
    field[cube] = "#"

#take y-coord in the middle and something, search to right until first "#" - the next char is in polygon
start_y = (min_y+max_y) // 2 + 1
for x in range(min_x, max_x):
    if field[x,start_y] == "#":
        start_x = x + 1
        break

#bfs
queue = deque([(start_x, start_y)])
while queue:
    current = queue.pop()
    neighbours = []
    for direction in directions.values():
        neighbour = tuple_sum(direction, current)
        neighbours.append(neighbour)
    for neighbour in neighbours:
        if field[neighbour] != "#":
            field[neighbour] = "#"
            queue.append(neighbour)

result = Counter(field.values())["#"]
print("Part 1:",result)
print("Runtime:", datetime.now() - time_start)