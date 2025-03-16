#Advent of Code 2023: Day 22
import re
from collections import defaultdict
from copy import deepcopy

def let_bricks_fall(bricks):
    counter = 0
    for brick_id in range(len(bricks)):
        max_z = 1
        falling = bricks[brick_id]
        for brick in bricks[:brick_id]:
            if bricks_overlay(falling, brick):
                max_z = max(max_z, brick[5] + 1)
        falling[5] = falling[5] - falling[2] + max_z
        if max_z != falling[2]:
            counter += 1
        falling[2] = max_z
    return bricks, counter

def bricks_overlay(brick1, brick2):
    x1_1, y1_1, z1_1, x2_1, y2_1, z2_1 = brick1
    x1_2, y1_2, z1_2, x2_2, y2_2, z2_2 = brick2
    return (max(x1_1, x1_2) <= min(x2_1, x2_2)) and (max(y1_1, y1_2) <= min(y2_1, y2_2))

def chain_reaction():
    #simulates fall of all bricks after disintegration of every single brick
    #exremely slow - about 30 mins for my data
    counter = 0
    for done, brick_id in enumerate(disintegrable):
        if done % 50 == 0:
            print(f"Done {done} of {len(disintegrable)}")
        new_bricks = deepcopy(bricks)
        _, diff = let_bricks_fall(new_bricks[:brick_id] + new_bricks[brick_id + 1:])
        counter += diff
    return counter

#MAIN
with open("test.txt") as file:
    raw_bricks = file.read().splitlines()

bricks = []
for brick in raw_bricks:
    bricks.append(list(map(int,(re.findall(r"\d+",brick)))))
bricks = sorted(bricks, key=lambda x: x[2])

bricks, _ = let_bricks_fall(bricks)

lower_on_upper = defaultdict(list)
upper_on_lower = defaultdict(list)

for id_upper, upper in enumerate(bricks):
    for id_lower, lower in enumerate(bricks[:id_upper]):
        if bricks_overlay(lower, upper) and lower[5]+1 == upper[2]:
            lower_on_upper[id_lower].append(id_upper)
            upper_on_lower[id_upper].append(id_lower)

disintegrable = set()
for upper, lower in upper_on_lower.items():
    if len(lower) == 1:
        disintegrable.add(lower[0])

print("Part 1:", len(bricks) - len(disintegrable))

print("Part 2:", chain_reaction())