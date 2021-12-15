from pprint import pprint
import sys
from collections import defaultdict
from enum import Enum

coords = []
folds = []

#with open('test.txt') as file:
with open('data.txt') as file:
    for line in file:
        line = line.rstrip()
        if not line:
            continue
        if ',' in line:
            x, y = line.split(',')
            coords.append((int(x),int(y)))
        else:
            section = line.split(' ')[2]
            direction, place = section.split('=')
            folds.append((direction, place))

# we have to determine the width and height based on the first two folds, rather than max location
# of a dot on the paper
first_folds = [
    folds[0],
    folds[1],
]

for axis, along in first_folds:
    size = (int(along) * 2) + 1 # + 1 is because the fold occurs on a line
    if axis == 'x':
        width = size
    else:
        length = size

assert length and width

row = ['.' for x in range(width)]
paper = [list(row) for y in range(length)]

def debug(paper: list):
    for i, row in enumerate(paper):
        line = ''
        for j, val in enumerate(row):
            line += val
        print(line)

def count_visible(paper: list) -> int:
    ret = 0

    for i, row in enumerate(paper):
        ret += row.count('#')

    return ret

def fold_y(paper: list, along: int) -> list:
    one = list(paper[0:along])
    two = list(paper[along:])
    two.reverse()
    row_len = len(one[0])

    for i, row in enumerate(two):
        for j, val in enumerate(row):
            if val == '#':
                one[i][j] = val

    return one

def fold_x(paper: list, along: int) -> list:
    one = []
    two = []

    for i, row in enumerate(paper):
        new_row_one = []
        new_row_two = []
        for j, val in enumerate(row):
            if j < along:
                new_row_one.append(val)
            else:
                new_row_two.append(val)
        one.append(new_row_one)
        new_row_two.reverse()
        two.append(new_row_two)

    for i, row in enumerate(two):
        for j, val in enumerate(row):
            if val == '#':
                one[i][j] = '#'

    return one

for col, row in coords:
    paper[row][col] = '#'

folded = paper
answer1 = None

for axis, along in folds:
    assert axis == 'y' or axis == 'x'

    if axis == 'x':
        folded = fold_x(list(folded), int(along))
    else:
        folded = fold_y(list(folded), int(along))

    debug(folded)
    if not answer1:
        answer1 = count_visible(folded)

# part 1
pprint(answer1)

# part 2
debug(folded)
