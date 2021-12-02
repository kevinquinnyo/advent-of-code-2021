#!/usr/bin/python3
from pprint import pprint

horiz = 0
depth = 0

with open('data.txt') as file:
    for line in file:
        direction, amt = line.rstrip().split(" ")
        amt = int(amt)
        if direction == 'forward':
            horiz += amt
        else:
            amt = amt if direction == 'down' else amt * -1
            depth += amt

pprint(horiz * depth)
