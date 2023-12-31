#Advent of Code 2023: Day 11:
from itertools import combinations

def ext_manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def create_space(lines):
    space = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                space.add((x,y))
    return space, x, y

def count_distances_between_stars(multiplikator):
    pairs = combinations(space, 2)
    distances = []
    for pair in pairs:
        first, second = pair
        x1, y1 = first
        x2, y2 = second
        #yellow block is written by me
        """        
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        delta_x = list(filter(lambda delta: x1 < delta < x2, empty_x))
        delta_y = list(filter(lambda delta: y1 < delta < y2, empty_y))
        """
        #simplified version via ChatGPT
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        delta_x = [delta for delta in empty_x if x1 < delta < x2]
        delta_y = [delta for delta in empty_y if y1 < delta < y2]

        distances.append(ext_manh_distance(first, second) +
                         len(delta_x) * (multiplikator-1) + len(delta_y) * (multiplikator-1))
    return sum(distances)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

space, max_x, max_y = create_space(lines)

#find all rows and cols with no stars in it
empty_x = list(range(max_x+1))
empty_y = list(range(max_y+1))
for star in space:
    x,y = star
    if x in empty_x:
        empty_x.remove(x)
    if y in empty_y:
        empty_y.remove(y)

print("Part 1:", count_distances_between_stars(2))
print("Part 2:", count_distances_between_stars(1000000))