#Advent of Code 2023: Day 22
from collections import defaultdict

def generate_cubies(brick):
    cubes = set()
    x1, y1, z1, x2, y2, z2 = brick
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                cubes.add((x,y,z))
    return cubes

def overlapping(brick): #generate a set of single cubies in brick for (x,y) only, Z is not relevant
    cubes = set()
    x1, y1, z1, x2, y2, z2 = brick
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            cubes.add((x, y))
    return cubes

def bricks_lying_under(sitting_over):
    lying_under = defaultdict(list)
    for under, over in sitting_over.items():
        for brick_over in over:
            lying_under[brick_over].append(under)
    return lying_under

#MAIN
with open("data.txt")as file:
    lines = file.read().splitlines()

bricks = []
for line in lines:
    brick = list(map(int, line.replace("~",",").split(",")))
    bricks.append(brick)
bricks = sorted(bricks, key=lambda x: x[2])

positions_taken = set()
for brick in bricks:
    fall_down = True
    cubes = generate_cubies(brick)
    while fall_down:
        brick[2] -= 1
        brick[5] -= 1
        one_cube_down = generate_cubies(brick)
        if positions_taken & one_cube_down or min(brick[2], brick[5]) <= 0:
            positions_taken |= cubes
            fall_down = False
        else:
            cubes = one_cube_down

sitting_over = dict()
for index, brick in enumerate(bricks):
    sitting_over[index] = []
    current_z = brick[2]
    tested_bricks = [brick_over for brick_over in bricks if brick_over[2] == current_z +1]
    cubes_current = overlapping(brick)
    for tested_brick in tested_bricks:
        cubes_tested = overlapping(tested_brick)
        if cubes_current & cubes_tested:
            sitting_over[index].append(bricks.index(tested_brick))
print(sitting_over)

lying_under = bricks_lying_under(sitting_over)

may_not_be_disintegrated = set()
for under, bricks_over in sitting_over.items():
    all_over = [item for sublist in sitting_over.values() for item in sublist]
    for brick_over in bricks_over:
        if all_over.count(brick_over) == 1:
            may_not_be_disintegrated.add(under)
print(len(may_not_be_disintegrated))