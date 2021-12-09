from pprint import pprint
from collections import defaultdict
import sys

matrix = []

#with open('test.txt') as file:
with open('data.txt') as file:
    for row in file:
        matrix.append([int(n) for n in row.rstrip()])

HEIGHT = len(matrix)
WIDTH = len(matrix[0])
MAX_NUM = 9

def down(i, j):
    new = i + 1
    if new > HEIGHT + 1:
        return (-1, -1)
    return (i + 1, j)

def up(i, j):
    new = i - 1
    if new < 0:
        return (-1, -1)
    return (new, j)

def left(i, j):
    new = j - 1
    if new < 0:
        return (-1, -1)
    return (i, new)

def right(i, j):
    new = j + 1
    if new > WIDTH - 1:
        return (-1, -1)
    return (i, new)

# low point hash map indexed by tuple of row (i), col (j)
low_points = {}
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        coords = [
            up(i, j),
            down(i, j),
            left(i, j),
            right(i, j),
        ]

        conditions = []
        for i2, j2 in coords:
            try:
                if (i2, j2) == (-1, -1):
                    raise IndexError('off map')
                else:
                    conditions.append(matrix[i2][j2] > num)
            except IndexError:
                conditions.append(True) # off map in any way is considered higher

        if all(conditions):
            low_points[(i, j)] = num + 1 # + 1 is "risk level"

# part 1
pprint(sum(low_points.values()))

basins = {}

def dfs(pos, low_point):
    i, j = pos

    if i < 0 or j < 0:
        return False

    if i > HEIGHT or j > WIDTH:
        return False

    try :
        if matrix[i][j] == MAX_NUM:
            return False
    except IndexError:
        return False

    # we walked every direction around low point and hit an already visited position
    if (i, j) in basins[low_point]:
        return basins[low_point]

    basins[low_point].add((i, j))

    dfs(up(i, j), low_point)
    dfs(down(i, j), low_point)
    dfs(left(i, j), low_point)
    dfs(right(i, j), low_point)

for low_point in low_points.keys():
    basins[low_point] = set()
    dfs(low_point, low_point) # original low_point is just used as a unique key for basins

result = []
for k, basin in basins.items():
    result.append(len(basin))

result.sort()
result.reverse()

answer = 1
for n in result[:3]:
    answer *= n

pprint(answer)
