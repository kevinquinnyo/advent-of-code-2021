#!/usr/bin/python3
from pprint import pprint

# FIXME: i have a feeling there is a bitwise magic trick that makes this simpler

BIT_LENGTH = 12
result = [0] * BIT_LENGTH

with open('data.txt') as file:
    for line in file:
        line = list(line.rstrip())
        for i in range(len(line)):
            if int(line[i]):
                result[i] += 1
            else:
                result[i] -= 1;

# convert our array of negative or positive numbers back to binary as string
gamma = ''.join('1' if n > 0 else '0' for n in result)
epsilon = ''.join('1' if n < 0 else '0' for n in result)

# convert to decimal
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

pprint(gamma * epsilon)
