#!/usr/bin/python3

with open('data.txt') as file:
    for row in file:
        positions = [int(n) for n in row.rstrip().split(',')]
        continue

# arithmetic sum formula (1 + 2 + 3 ... n)
def fuel_cost(n):
    return (n / 2) * (1 + n)

# there is probably a math magic trick somewhere to make this faster
# brute force for now..

# part 1
lowest = 999999999999999999999
for guess in range(min(positions), max(positions)):
    cost = 0
    for n in positions:
        cost += abs(n - guess)
    if cost < lowest:
        lowest = cost

print(lowest)

# part 2
lowest = 999999999999999999999
for guess in range(min(positions), max(positions)):
    cost = 0
    for n in positions:
        cost += fuel_cost(abs(n - guess))
    if cost < lowest:
        lowest = cost

print(lowest)
