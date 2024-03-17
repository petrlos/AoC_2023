#Advent of Code 2023: Day 23

from collections import deque

def find_longest_path(map):
    queue = deque([0])

    visited = {0: 0}
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

maps = []
#key = start node; value = (end node, distance)
maps.append ({
    0: [(1,15)],
    1: [(4,22), (2,22)],
    2: [(5,24), (3 ,30)],
    3: [(7,10)],
    4: [(6,38), (5,12)],
    5: [(6,10), (3,18)],
    6: [(7,10)],
    7: [(8,5)],
    8: []
})

maps.append({
    0: [(1,2)],
    1: [(2,4), (2,10)],
    2: [(3,7)],
    3: []
})


#MAIN
for map in maps:
    result = find_longest_path(map)
    print("Result:", result[max(result.keys())])

#works on test data - coutned and imported manually
