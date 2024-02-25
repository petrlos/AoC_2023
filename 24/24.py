#Advent of Code 2023: Day 24
from itertools import combinations
import re
import sympy

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

#part2
def checker(numbers):
    #function to check the equations for sympy using known values of startcoords of rock and its vector
    #not used for data, only for testing
    a, b, c, da, db, dc = [24,13,10,-3,1,2]
    x0, y0, z0, dx, dy, dz = numbers
    print(f" x vs. y {(x0 - a) * (db - dy) - (y0 - b) * (da - dx)}", end="")
    print(f" x vs. z {(x0 - a) * (dc - dz) - (z0 - c) * (dc - dx)}", end="")
    print(f" y vs. z {(y0 - b) * (dc - dz) - (z0 - c) * (db - dy)}")

with open("data.txt") as file:
    lines = file.read().splitlines()

a, b, c, da, db, dc = sympy.symbols("a, b, c, da, db, dc")

equations = []
for line in lines[:4]:
    numbers = list(map(int,(re.findall(r"-?\d+",line))))
    x0, y0, z0, dx, dy, dz = numbers
    equations.append((x0 - a) * (db - dy) - (y0 - b) * (da - dx))
    equations.append((y0 - b) * (dc - dz) - (z0 - c) * (db - dy))

answers = sympy.solve(equations)
print(answers[0])
print("Part 2:",answers[0][a] + answers[0][b] + answers[0][c])