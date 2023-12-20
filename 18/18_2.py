#Advent of Code 2023: Day 18 - Vs.2
#Area of Polygon counted via Coordinate Geometry

def find_vertices(lines, part1=True):
    x, y = 0,0
    vertices = []
    dir = dict(zip(("0123"), ("RDLU")))
    border = 0
    for line in lines:
        direction, count, colour = line.split(" ")
        if part1:
            count = int(count)
        else:
            direction = dir[colour[-2]]
            count = int(colour[2:-2], 16)
        border += count
        dir_x, dir_y = directions[direction]
        x, y = x + dir_x * count, y + dir_y*count #one coordine in direction is always zero
        vertices.append((x,y))
    return vertices, border

def shoelace_formula(vertices, border):
    result = 0
    for i in range(len(vertices)):  # x1y2 + x2y3 + x3y4 + ... + x(n)y1
        x = vertices[i][0]
        y = vertices[(i + 1) % len(vertices)][1]
        result += x * y
    for i in range(len(vertices)): # -x2y1 - x3y2 - x4y3 - ... - x1y(n)
        x = vertices[(i + 1) % len(vertices)][0]
        y = vertices[i][1]
        result -= x * y
    result = result // 2
    # shoelace formula counts area in the middle of the grid squares - 1/2 border must be added
    return result + border // 2 + 1

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}  # UDLR

part1 = True #function recycling, muhaha :D
for i in range(1,3):
    vertices, border = find_vertices(lines, part1)
    result = shoelace_formula(vertices, border)
    print("Part {0}: {1}".format(i, result))
    part1 = False