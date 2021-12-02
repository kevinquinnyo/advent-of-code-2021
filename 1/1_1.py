#!/usr/bin/python3
from pprint import pprint

count = 0
last = None

with open('data.txt') as file:
    for line in file:
        n = int(line.rstrip())
        if last is not None and n > last:
            count += 1;
        last = n

pprint(count)
