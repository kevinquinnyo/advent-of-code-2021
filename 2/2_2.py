#!/usr/bin/python3
from pprint import pprint

forw = 0
aim = 0
depth = 0

with open('data.txt') as file:
    for line in file:
        direction, amt = line.rstrip().split(" ")
        amt = int(amt)

        if direction == 'down':
            aim += amt
            continue
        if direction == 'up':
            aim -= amt
            continue
        if direction == 'forward':
            forw += amt
            depth_increase = amt * aim
            depth += depth_increase

pprint(forw * depth)
