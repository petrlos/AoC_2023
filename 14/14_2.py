#Advent of Code 2023: Day 14
import numpy as np

def load_board(lines):
    board = np.zeros((max_x, max_y)) #empty slots = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "O": #movable stones = 1
                board[(x, y)] = 1
            elif char == "#": #non-movable stones = -1
                board[(x, y)] = -1
    return board

def count_load(board):
    #slice numpy array in rows from top to bottom, count rocks (==1), multiply by row_index, sumup
    return sum([(max_y - y) * np.count_nonzero(board[y, :] == 1) for y in range(max_y)])

def slide_single_column_up(row):
    new_row = []
    for segment in row.split("#"):
        stones_count = segment.count("O")
        #move all zeros in segment left, fill up with dots
        new_row.append("O"*stones_count + "."* (len(segment) - stones_count))
    return "#".join(new_row)

def slide_all_columns_up(board):
    there = {0:".", 1:"O", -1:"#"}
    back = {".": 0, "#":-1, "O":1}
    for y in range(max_y):
        column = [int(num) for num in board[:, y]] #convert all numpy numbers to int
        column_str = "".join([there[char] for char in column]) #translate column to string
        column_slided = slide_single_column_up(column_str)
        for x in range(max_x-1, -1, -1):
            board[(x,y)] = back[column_slided[x]]
    return board

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

max_x, max_y = len(lines[0]), len(lines)

#Part 1:
board = slide_all_columns_up(load_board(lines))
print("Part 1:", count_load(board))