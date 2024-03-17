#Advent of Code 2023: Day 23
from collections import deque

def bfs(node, map, nodes): #find shortest path to each nearest node
    slopes = "><v^"
    dist = {node: 0}
    queue = deque([node])
    visited = set()
    result = []
    while queue:
        current = queue.popleft()
        for index, direction in enumerate(directions):
            neighbour = tuple_sum(direction, current)
            if neighbour in map and neighbour not in visited and neighbour not in nodes:
                if map[neighbour] != slopes[index]:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    dist[neighbour] = dist[current] + 1
            if neighbour in nodes and neighbour != node:
                result.append((neighbour, dist[current]+1))
    return {node: result}

def parse_map(lines):
    max_row = len(lines)
    max_col = len(lines[0])
    map = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != "#":
                map[(row, col)] = char
    nodes = {(0,1), (max_row-1, max_col-2)} #start + end
    for key, value in map.items():
        neighbours = set([tuple_sum(direction, key) for direction in directions])
        if sum([neighbour in map for neighbour in neighbours]) >= 3:
            nodes.add(key) #intersection must have 3 non-"#" at least
    distances = dict()
    for node in nodes: #shortest distance to each node not passing through other nodes
        distances.update(bfs(node, map, nodes))
    return distances

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def find_longest_path(map):
    queue = deque([(0,1)])

    visited = {(0,1): 0} #distance to start is zero
    while queue:
        current = queue.popleft()
        for value in map[current]:
            node, distance = value
            if node not in visited.keys():
                visited[node] = visited[current] + distance
                queue.append(node)
            elif visited[current] + distance > visited[node]:
                visited[node] = visited[current] + distance
                queue.append(node)
    return visited

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] #LRUD

#return compressed graph - from each intersection distance to nearest possible
distances = parse_map(lines)

#longest path from start to each node
results = find_longest_path(distances)

#max = key with highest row = the bottom one
print("Result:", results[max(results.keys())])