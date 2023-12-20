#Advent of Code 2023: Day 13
import numpy as np
from datetime import datetime
time_start = datetime.now()

def generate_numpy_grid(pattern):
    pattern = pattern.replace("#","1").replace(".","0")
    number_grid = []
    for line in pattern.splitlines():
        number_grid.append(list(map(int, list(line))))
    number_grid = np.array(number_grid)
    return number_grid

def find_smudge(current_grid, difference):
    width = current_grid.shape[1]
    for midpoint in range(1, width):
        left = current_grid[:, :midpoint]  # cut array left from midpoint
        right = current_grid[:, midpoint:] # cut array right from midpoint
        left_width, right_width = left.shape[1], right.shape[1]
        cut_off = abs(left_width - right_width) #both arrays must have same width
        if left_width < right_width:
            right = right[:, :-cut_off]
        else:
            left = left[:, cut_off:]
        left = left[:, ::-1]  # reverse order of columns
        diff = abs(left - right)
        #Part1: difference must be zero - arrays are completely the same
        #Part2: number "1" may be only once in the difference of arrays
        if np.count_nonzero(diff == 1) == difference:
            return midpoint
    return -1

#MAIN
with open("data.txt") as file:
    patterns = file.read().split("\n\n")

part1s, part2s = [], []
for pattern in patterns:
    current_grid = generate_numpy_grid(pattern)
    part1 = find_smudge(current_grid, 0)
    part2 = find_smudge(current_grid, 1)
    if part1 == -1: #no midpoint found
        rotated = np.rot90(current_grid, k=1)
        part1 = 100 * find_smudge(rotated, 0)
    if part2 == -1: #no smudge found
        rotated = np.rot90(current_grid, k=1)
        part2 = 100 * find_smudge(rotated, 1)
    part1s.append(part1)
    part2s.append(part2)

print("Part 1", sum(part1s))
print("Part 2", sum(part2s))

print("Runtime:", datetime.now() - time_start)