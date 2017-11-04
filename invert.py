import sys
from sys import stdin
from Graph import Graph

filename = sys.argv[1]
delimiter = sys.argv[2]
graph = Graph(filename, delimiter)
for line in stdin:
    v = line.strip()
    # print(v, v in graph, tuple(graph.neighbours_of(v)))
    if v in graph:
        for w in graph.neighbours_of(v):
            print('\t' + w)
