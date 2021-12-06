#!/usr/bin/python3

# we can maybe calculate the rate of change based on the answer already provided for the test data
# for puzzle 2 but we can also just do this with less space complexity using a stack:

with open('data.txt') as file:
    for row in file:
        inp = [int(n) for n in row.rstrip().split(',')]
        continue

# We count down from 256 days, and shift the array over 1 to indicate that the timer
# decrements. The number on value 0 moves to the end of the array to indicate new fish being
# spawned. The only special case to handle is that we also increment the 6th index which represents
# those ancestor fish resetting their timer (per the puzzle conditions)

def answer(days: int, inp: list) -> int:
    # first make a list of the count of all "timers" (days until respawn)
    timers = [0] * 9
    for n in inp:
        timers[n] += 1

    while days:
        tmp = timers.pop(0)
        timers.append(tmp)
        timers[6] += tmp
        days -= 1

    return sum(timers)

print(answer(80, inp))
print(answer(256, inp))
