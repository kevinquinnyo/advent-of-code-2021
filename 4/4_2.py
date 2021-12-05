#!/usr/bin/python3
from pprint import pprint
from collections import defaultdict
import sys

data = []
with open('test.txt') as file:
#with open('data.txt') as file:
    nums = None;
    for line in file:
        line = line.rstrip()
        data.append(line)

nums = data.pop(0)
nums = nums.split(',')
boards = []
board = []

# hack, add a final '' delimiter to get the last board since we are splitting boards on ''
# and remove the first ''
data.append('')
data.pop(0)

for line in data:
    if line == '':
        boards.append(board)
        board = []
    else:
        row = line.split()
        board.append(row)

# index is board ID
bmap = {}

# we assume the boards are 5 for now and square
BOARD_SIZE = 5

winning_boards = []

'''
return (winning board_id, last num called) once there is a bingo
'''
def process(boards, nums) -> tuple:
    final_board = False
    for num in nums:
        for board_id, board in enumerate(boards):
            if board_id in winning_boards:
                continue
            if ((len(winning_boards) + 1) == len(boards)):
                final_board = True
            if board_id not in bmap:
                bmap[board_id] = defaultdict(int)
            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if val == num:
                        # mark position on board for later
                        board[i][j] = '#'

                        # hashmap keys. we need a horizontal and vertical
                        i_key = 'I_{}'.format(i)
                        j_key = 'J_{}'.format(j)

                        bmap[board_id][i_key] += 1
                        bmap[board_id][j_key] += 1

                        if bmap[board_id][j_key] >= BOARD_SIZE or bmap[board_id][i_key] >= BOARD_SIZE:
                            if final_board:
                                return (board_id, num)

                            winning_boards.append(board_id)

    # throw probably instead
    return ([], -1)

def calculate_winning_board(board: list, last_num: int) -> int:
    final_sum = 0
    for row in board:
        for val in row:
            if val != '#':
                final_sum += int(val)

    return final_sum * last_num;

result = process(boards, nums)
pprint(boards)
pprint(result)
board = boards[result[0]]
last_num = int(result[1])

pprint(calculate_winning_board(board, last_num))
