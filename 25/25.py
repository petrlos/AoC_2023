#Advent of Code 2023: Day 25
import networkx as nx
from datetime import datetime
time_start = datetime.now()

def create_graph(lines):
    graph = nx.Graph()
    for line in lines:
        left, right = line.split(": ")
        for node in right.split(" "):
            graph.add_edge(left, node)
            graph.add_edge(node, left)
    return graph

#MAIN
with open("data.txt")as file:
    lines = file.read().splitlines()

graph = create_graph(lines)

edges_to_be_removed = nx.minimum_edge_cut(graph) #find pairs of nodes, those edges must be cut

print("These edges must be removed:", edges_to_be_removed)

graph.remove_edges_from(edges_to_be_removed) #remove those edges from graph

first, second = nx.connected_components(graph) # find which nodes are connected

print("Size of part1:", len(first))
print("Size of part2:", len(second))
print("Result:", len(first) * len(second)) #return product
print("Total runtime:", datetime.now() - time_start)