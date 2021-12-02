#!/usr/bin/python3
from pprint import pprint
import sys

count = 0
prev = []
stack = []

with open('data.txt') as file:
    for line in file:
        n = int(line.rstrip())
        stack.append(n)

        while len(stack) == 3:
            if prev and sum(stack) > sum(prev):
                count += 1
            prev = list(stack)
            stack.pop(0)

pprint(count)
