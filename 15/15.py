from pprint import pprint
import sys
from collections import defaultdict, Counter
import math
from copy import deepcopy
import heapq

"""
Note for day 15: I fumbled around with BFS and recursive DFS for a long time before finally looking
for a hint on https://reddit.com/r/adventofcode.  That's when I noticed the Djikstra algorithm being
talked about. See note below. I lifted that algorithm directly from a git repo as-is. This was a
tough one. I basically cheated and it was still hard.
"""
matrix = []

#with open('test.txt') as file:
with open('data.txt') as file:
    for line in file:
        line = line.rstrip()
        row = [int(n) for n in line]
        matrix.append(row)

def valid_position(point: tuple, matrix: list):
    i, j = point
    length = len(matrix)
    width = len(matrix[0])

    if i < 0 or i >= length:
        return False

    if j < 0 or j >= width:
        return False

    return True

"""
NOTE: Borrowed (stolen) from https://github.com/TheAlgorithms/Python/blob/master/graphs/dijkstra.py
"""
def dijkstra(graph, start, end):
    """Return the cost of the shortest path between vertices start and end.
    """
    heap = [(0, start)]  # cost from start node,end node
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return -1

"""
All we have to do is build an adjacency list to plug into our borrowed (stolen) djikstra algorithm.
"""
def build_adjacency_list(matrix: list):
    adj = defaultdict(list)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            points = [
                (i - 1, j),
                (i + 1, j),
                (i, j + 1),
                (i, j - 1)
            ]

            node = (i, j)
            neighbors = [point for point in points if valid_position(point, matrix)]

            for neighbor in neighbors:
                ni, nj = neighbor
                cost = matrix[ni][nj]

                adj[node].append([neighbor, cost])
    return adj

# part 1
length = len(matrix)
width = len(matrix[0])
start = (0, 0)
end = (length - 1, width - 1)

adj = build_adjacency_list(matrix)
pprint(dijkstra(adj, start, end))

# part 2
def expand(matrix, times):
    def increase_risks(risks: list) -> list:
        return [risk + 1 if risk < 9 else 1 for risk in risks]

    L = len(matrix)
    W = len(matrix[0])

    new_matrix = deepcopy(matrix)

    for n in range(1, times):
        for row in new_matrix:
            window = row[-W:] # always take the last W items where W is the original width
            row.extend(increase_risks(window))

    for n in range(1, times):
        for row in new_matrix[-L:]: # always take last L rows where L is the original num of rows
            new_matrix.append(increase_risks(row))

    return new_matrix

new_matrix = expand(matrix, 5)

length = len(new_matrix)
width = len(new_matrix[0])
start = (0, 0)
end = (length - 1, width - 1)

adj = build_adjacency_list(new_matrix)
pprint(dijkstra(adj, start, end))
