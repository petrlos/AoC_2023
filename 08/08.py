#Advent of Code 2023: Day 8
def parse_nodes(lines):
    nodes = {}
    for line in lines:
        key, value = line.split(" = ")
        value = value[1:-1].split(", ")
        nodes[key] = value
    return nodes

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

path = [0 if step == "L" else 1 for step in lines[0]]
nodes = parse_nodes(lines[2:])

current = "AAA"
counter = 0
while current != "ZZZ":
    direction = path[counter % len(path)]
    current = nodes[current][direction]
    counter += 1
print("Part 1:",counter)