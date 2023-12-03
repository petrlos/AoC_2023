#Advent of Code  2023: Day 3
import re
from datetime import datetime
time_start = datetime.now()

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def symbol_around(number, current, index):
    surroundings = ""
    number = str(number)
    for x in range(len(number)):
        cipher_coord = (x+index, current)
        for surroundings_delta_coord in surroundings_delta_coords:
            new_coord = tuple_sum(surroundings_delta_coord, cipher_coord)
            if new_coord in grid.keys():
                surroundings += grid[new_coord]
                if grid[new_coord] == "*": #for part2: if star found, save tested number to star coord
                    stars[new_coord].add(int(number))
    #remove from surroundings everything except numbers
    symbols = list(filter(lambda x: x != ".", re.findall(r"\D", surroundings)))
    return len(symbols)

def parse_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                grid[(x,y)] = char
    return grid

def test_neighbours(lines):
    sumup = 0
    for current, line in enumerate(lines):
        regex = re.compile(r'\d+')
        #find all numbers on line and index of first cipher
        numbers = [(match.group(), match.start()) for match in regex.finditer(line)]
        for number, index in numbers:
            if symbol_around(number, current, index):
                sumup += int(number)
    return sumup

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = parse_grid(lines)

stars = {} #save coords of all stars for part2
for coord, char in grid.items():
    if char == "*":
        stars[coord] = set()

surroundings_delta_coords = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
surroundings_delta_coords.remove((0,0))

#Part1
print("Part 1:",test_neighbours(lines))

#Part2
sumup_part2 = 0
for pair in stars.values():
    if len(pair) == 2: #all stars with two members only
        x,y = pair
        sumup_part2 += x * y

print("Part 2:",sumup_part2)
print("Runtime:", datetime.now()-time_start)