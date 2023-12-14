#Advent of Code 2023: Day 14

def parse_platform(lines):
    platform = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                platform[(x,y)] = char
    return platform, x, y

def print_platform(platform, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in platform.keys():
                print(platform[(x,y)], end="")
            else:
                print(".", end="")
        print(" ")

def count_load(platform, max_y):
    total_load = 0
    for coord, rock in platform.items():
        if rock == "O":
            total_load += max_y - coord[1] + 1
    return total_load

def move_up_possible(x,y):
    return  (x,y-1) not in platform.keys() and y > 0

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

platform, max_x, max_y = parse_platform(lines)

for x in range(max_x+1):
    for y in range(max_y+1):
        if (x,y) in platform.keys():
            if platform[(x,y)] == "O":
                new_y = y
                while move_up_possible(x,new_y):
                    new_y -= 1
                platform.pop((x,y))
                platform[(x,new_y)] = "O"

print("Part 1:",count_load(platform, max_y))