#Advent of Code 2023: Day 8
from math import lcm

def parse_nodes(lines):
    nodes = {}
    for line in lines:
        key, value = line.split(" = ")
        value = value[1:-1].split(", ")
        nodes[key] = value
    return nodes

def get_path_length(start, end): #works for part1 and part2
    current = start
    counter = 0
    while current not in end:
        direction = path[counter % len(path)]
        current = nodes[current][direction]
        counter += 1
    return counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

path = [0 if step == "L" else 1 for step in lines[0]]
nodes = parse_nodes(lines[2:])

print("Part 1:",get_path_length("AAA", ["ZZZ"])) #second parameter must be list because of part2

possible_starts = []
possible_ends = []
for key in nodes.keys():
    if key[-1] == "A":
        possible_starts.append(key)
    if key[-1] == "Z":
        possible_ends.append(key)

lengths = []
for start in possible_starts: #check path length from each start to any end
    lengths.append(get_path_length(start, possible_ends))
print("Part 2",lcm(*lengths)) #get least common multiple