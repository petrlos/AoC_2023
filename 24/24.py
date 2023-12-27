#Advent of Code 2023: Day 24
from itertools import combinations
import re

def intersection_found(first, second, lower=200000000000000, upper=400000000000000):
    x1,y1,z1, dx1,dy1,dz1= list(map(int,(re.findall(r"-?\d+",first))))
    x2,y2,z2, dx2,dy2,dz2 = list(map(int,(re.findall(r"-?\d+",second))))
    denominator = dx1*dy2 - dy1*dx2
    if denominator == 0:
        return False
    t_int = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / denominator
    int_x, int_y = x1 + t_int*dx1, y1 + t_int*dy1
    if lower <= int_x <= upper and lower <= int_y <= upper:
        tx1 = (int_x - x1) / dx1
        tx2 = (int_x - x2) / dx2
        if tx1 < 0 or tx2 < 0:
            return False
        return True
    return False

def part1(lines):
    pairs = combinations(lines, 2)
    counter = 0
    for pair in pairs:
        first, second = pair
        if intersection_found(first, second):
            counter += 1
    return counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

part1 = part1(lines)
print("Part 1:", part1)