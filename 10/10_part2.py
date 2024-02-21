#Advent of Code 2023: Day 10 - Part 2
def check_points(line):
    inside = False
    counter = 0
    last_bend = ""
    for char in line:
        if char == "-":
            continue
        if char == "|":
            inside = not inside
        if char in "LF":
            last_bend = char
        if char == "7" and last_bend == "L":
            inside = not inside
        if char == "J" and last_bend == "F":
            inside = not inside
        if inside and char == ".":
            counter +=1
    return counter


with open("test.txt") as file:
    lines = file.read().splitlines()

print(check_points("|F|F-JF---7...L7L|7|"))


total_sum = 0
for line in lines:
    total_sum += check_points(line)

print(total_sum)