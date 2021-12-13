from pprint import pprint
import sys


#- First, the energy level of each octopus increases by 1.
# - Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
# - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.


matrix = []
#with open('test.txt') as file:
with open('data.txt') as file:
    for line in file:
        matrix.append([int(n) for n in line.rstrip()])

LENGTH = len(matrix)
WIDTH = len(matrix[0])

STEP_FLASHES = {}
STEP_COUNTS = {}

def valid_position(point: tuple):
    i, j = point

    if i < 0 or i >= LENGTH:
        return False

    if j < 0 or j >= WIDTH:
        return False

    return True

def get_neighbors(point: tuple) -> list:
    i, j = point

    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    upright = (i - 1, j + 1)
    upleft = (i - 1, j - 1)
    downright = (i + 1, j + 1)
    downleft = (i + 1, j - 1)

    points = [
        up,
        down,
        left,
        right,
        upright,
        upleft,
        downright,
        downleft,
    ]

    return [point for point in points if valid_position(point)]

def increase_energy(point: tuple, step: int):
    i, j = point
    flash = False

    matrix[i][j] += 1

    if matrix[i][j] > 9:
        flash = True

    if flash and point not in STEP_FLASHES[step]:
        STEP_FLASHES[step].add((i, j))

        for ni, nj in get_neighbors(point):
            increase_energy((ni, nj), step)

def reset_flashers(step: int):
    # cache how many flashed this step at the same time for part 2
    if step not in STEP_COUNTS:
        STEP_COUNTS[step] = 0

    STEP_COUNTS[step] = len(STEP_FLASHES[step])

    for flasher in STEP_FLASHES[step]:
        fi, fj = flasher
        if matrix[fi][fj] > 9:
            matrix[fi][fj] = 0

def process_step(step: int):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            increase_energy((i, j), step)
    reset_flashers(step)

def part1(num_steps: int):
    for step in range(1, num_steps + 1):
        if step not in STEP_FLASHES:
            STEP_FLASHES[step] = set()

        process_step(step)

part1(100)

answer = 0
for flashes in STEP_FLASHES.values():
    answer += len(flashes)

# part 1
pprint(answer)

# we mutate the matrix in place so we have to do everything fresh for part 2
matrix = []
#with open('test.txt') as file:
with open('data.txt') as file:
    for line in file:
        matrix.append([int(n) for n in line.rstrip()])

LENGTH = len(matrix)
WIDTH = len(matrix[0])

STEP_FLASHES = {}
STEP_COUNTS = {}
def part2():
    step = 1

    while step < 1e9:
        if step not in STEP_FLASHES:
            STEP_FLASHES[step] = set()

        process_step(step)

        if step in STEP_COUNTS and STEP_COUNTS[step] == WIDTH * LENGTH:
            return step

        step += 1

# part 2
pprint(part2())
