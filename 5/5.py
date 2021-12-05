#!/usr/bin/python3
from pprint import pprint
from collections import defaultdict
import sys

#Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
#
#    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

# to solve this we just use a hash map for every point the lines cross. probably a faster way

class Point:
    x = None
    y = None

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def new_from_csv(csv: str):
        x, y = csv.split(',')

        return Point(x, y)

    '''
    just for quick debugging of the object
    '''
    def __str__(self) -> str:
        return '{},{}'.format(self.x, self.y)

# straight (horizontal or vertical only now) line
class Line:
    start = None
    end = None

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    '''
    just for quick debugging of the object
    '''
    def __str__(self) -> str:
        return '{} -> {}'.format(self.start, self.end)

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_straight(self) -> bool:
        return self.is_vertical() or self.is_horizontal()

    '''
    NOTE: We assume that if it's not straight then it's a 45 degree angle due to puzzle criteria
    '''
    def is_diagonal(self) -> bool:
        return not self.is_straight()

    def get_coverage_map(self) -> list:
        cov = []

        if self.is_horizontal():
            for i in self.get_range(self.start.x, self.end.x):
                cov.append('{}.{}'.format(i, self.start.y))

            return cov

        if self.is_vertical():
            for i in self.get_range(self.start.y, self.end.y):
                cov.append('{}.{}'.format(self.start.x, i))

            return cov

        '''
        45 deg case
        example: (0,8) -> (3,5)
            (0,8), (1,7), (2,6), (3,5)
            hashes: 0.8, 1.7, 2.6, 3.5
        '''
        start = self.start
        end = self.end

        # calculate slope (this will be 1 or -1)
        m = (end.y - start.y) / (end.x - start.x)

        # normalize so we always track a slope left to right
        if end.x < start.x:
            tmp = start
            start = end
            end = tmp

        x = start.x
        y = start.y

        # dist of line segment easy because we know it's 45 deg
        dist = abs(start.x - end.x) + 1
        while dist:
            # add entry to hashmap for every point along the slope
            cov.append('{}.{}'.format(x, y))
            if m < 1:
                x += 1
                y -= 1
            else:
                x += 1
                y += 1

            dist -= 1

        return cov

    def get_range(self, one: int, two: int):
        if two < one:
            tmp = one
            one = two
            two = tmp

        # range needs ascending values but also does not include the last value
        return range(one, two + 1)


def build_coverage_map(include_diag: bool = False):
    coverage = defaultdict(int)
    with open('test.txt') as file:
    #with open('data.txt') as file:
        for row in file:
            row = row.rstrip()
            start, end = row.split(' -> ')

            start = Point.new_from_csv(start)
            end = Point.new_from_csv(end)

            line = Line(start, end)

            if not include_diag and not line.is_straight():
                continue

            for key in line.get_coverage_map():
                coverage[key] += 1
    return coverage

# puzzle 1
coverage = build_coverage_map()

c = 0
for n in coverage.values():
    if n > 1:
        c += 1

pprint(c)

# puzzle 2
coverage = build_coverage_map(include_diag=True)

c = 0
for n in coverage.values():
    if n > 1:
        c += 1

pprint(c)
