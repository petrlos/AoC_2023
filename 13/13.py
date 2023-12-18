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

def generate_columns(midpoint, width):
    #returns indexes of corresponding columns for comparison
    #e.g. mirrors between 3/4, must compare 3/4, 2/5, 1/6 and 0/7
    left = list(range(midpoint, 0, -1))
    right = list(range(midpoint+1, width+1))
    return left, right

def compare_columns(left_col_index, right_col_index, current_grid):
    #if left or right runs out, for cycle ends
    for col1, col2 in zip(left_col_index, right_col_index):
        left = current_grid[:, col1-1]
        right = current_grid[:, col2-1]
        if not np.array_equal(left, right):
            return False
    return True

def find_column_of_reflection(current_grid, width):
    result = -1 # no reflection found
    for midpoint in range(1, width): #1 == reflects between 0/1, etc.
        left_col_index, right_col_index = generate_columns(midpoint, width)
        if compare_columns(left_col_index, right_col_index, current_grid):
            return midpoint #no more comparison needed
    return result

#MAIN
with open("data.txt") as file:
    patterns = file.read().split("\n\n")

results = []
for pattern in patterns:
    current_grid = generate_numpy_grid(pattern) #create a numpy field of zeros and ones
    result = find_column_of_reflection(current_grid, current_grid.shape[1])
    if result == -1: #no result found - rotate by 90 deg counterCW and search again
        current_grid = np.rot90(current_grid, k=1)
        result = 100*find_column_of_reflection(current_grid, current_grid.shape[1])
    results.append(result)
print("Part 1:",sum(results))
print("Runtime:", datetime.now() - time_start)