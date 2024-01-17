#Advent of Code 2023: Day 22
from collections import defaultdict, Counter
from datetime import datetime
time_start = datetime.now()

def generate_cubes(brick): #generate all single cubes
    cubes = set()
    x1, y1, z1, x2, y2, z2 = brick
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                cubes.add((x,y,z))
    return cubes

def overlapping(brick): #generate a set of single cubes in brick for (x,y) only, Z is not relevant
    cubes = set()
    x1, y1, z1, x2, y2, z2 = brick
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            cubes.add((x, y))
    return cubes

def generate_bricks(lines):
    bricks = []
    for line in lines:
        brick = list(map(int, line.replace("~",",").split(",")))
        bricks.append(brick)
    return sorted(bricks, key=lambda x: x[2])

def let_the_bricks_fall(bricks):
    positions_taken = set()
    for brick in bricks:
        fall_down = True
        cubes = generate_cubes(brick)
        while fall_down:
            brick[2] -= 1
            brick[5] -= 1
            one_cube_down = generate_cubes(brick)
            if positions_taken & one_cube_down or min(brick[2], brick[5]) <= 0:
                positions_taken |= cubes
                fall_down = False
            else:
                cubes = one_cube_down
    return bricks

#MAIN
with open("data.txt")as file:
    lines = file.read().splitlines()

#generate list of sorted bricks from bottom to top in format "x1,y1,z1,x2,y2,z2"
bricks = generate_bricks(lines)
#check every single brick, if fall down possible, let it fall
bricks = let_the_bricks_fall(bricks)

#Find out which brick lies directly over (under) + overlaps
lying_over = defaultdict(set)   #key = lower brick, value = bricks lying upon
lying_under = defaultdict(set)  #key = upper brick, value = bricks lying underneath
for i, brick in enumerate(bricks):
    cubes_current = overlapping(brick) #only (x,y) coords
    tested_bricks = [brick_over for brick_over in bricks if brick_over[2] == brick[5] +1] #all bricks lying 1 step higher
    for tested_brick in tested_bricks:
        cubes_tested = overlapping(tested_brick) #only (x,y) coords
        if cubes_current & cubes_tested: #if any (x,y) matches - bricks overlap
            lying_over[i].add(bricks.index(tested_brick))
            lying_under[bricks.index(tested_brick)].add(i)

#Find out which bricks are NOT disintegrateable
not_disintegrateable = set()
for key, values in lying_over.items():
    for value in values:
        if len(lying_under[value]) == 1:
            not_disintegrateable.add(key)

print("Result:", len(bricks) - len(not_disintegrateable))
print("Runtime:", datetime.now() - time_start)