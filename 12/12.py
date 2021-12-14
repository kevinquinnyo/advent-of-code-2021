from pprint import pprint
import sys
from collections import defaultdict

# we create an adjacency list. this is an undirected graph so we add child->parent and vice versa
adj = defaultdict(set)

with open('test.txt') as file:
#with open('data.txt') as file:
    for line in file:
        parent, child = line.rstrip().split('-')
        adj[parent].add(child)
        adj[child].add(parent)

paths = []
path = []

def dfs(node: str, path: list):
    path.append(node)

    if node == 'end':
        paths.append(path)
        return

    for child in adj[node]:
        if child.islower() and child in path:
            continue

        # we must create a new list here or else we are mutating path in paths directly
        dfs(child, list(path))

dfs('start', [])

# part 1
pprint(len(paths))

# part 2
# TODO probably create a function that checks if a lower (not start or end) already exists?

