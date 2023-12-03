#Advent of Code  2023: Day 3
import re

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def symbol_around(number, current, where):
    surroundings = ""
    number = str(number)
    for x in range(len(number)):
        cipher_coord = (x+where, current)
        for surroundings_delta_coord in surroundings_delta_coords:
            new_coord = tuple_sum(surroundings_delta_coord, cipher_coord)
            if new_coord in grid.keys():
                surroundings += grid[new_coord]
    symbols = list(filter(lambda x: x != ".", re.findall(r"\D", surroundings)))
    return len(symbols)

def parse_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                grid[(x,y)] = char
    return grid

def part1(lines):
    sumup = 0
    for current, line in enumerate(lines):
        regex = re.compile(r'\d+')
        matches = regex.finditer(line)
        numbers = [(match.group(), match.start()) for match in matches]
        for number, where in numbers:
            if symbol_around(number, current, where):
                sumup += int(number)
    return sumup

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid = parse_grid(lines)
surroundings_delta_coords = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
surroundings_delta_coords.remove((0,0))

print("Part 1:",part1(lines))


