from pprint import pprint
from collections import defaultdict
from itertools import permutations
import sys

lines = []

with open('data.txt') as file:
    for row in file:
        lines.append(row.rstrip().split(' | '))

# puzzle 1:
answer = 0
for line in lines:
    _, output = line
    words = [word for word in output.split()]
    for word in words:
        if len(word) in [2, 3, 4, 7]:
            answer += 1
pprint(answer)

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# brute force, sigh.  TODO try to solve this again using deduction
KNOWN = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdgf',
}

def create_words(permutation, template):
    # lazy
    known = {k: list(v) for k, v in template.items()}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    _map = dict(zip(letters, list(permutation)))
    new_map = {}

    for k, chars in known.items():
        new_map[k] = [_map[c] for c in chars]

    # convert it back to a simple list of words as strings
    return [''.join(sorted(c)) for c in new_map.values()]

def get_perms():
    for p in permutations('abcdefg'):
        yield p

# test = ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
answer = 0

for line in lines:
    words, output = line
    words = [''.join(sorted(w)) for w in words.split()]
    output = [''.join(sorted(w)) for w in output.split()]

    found = None

    for p in get_perms():
        guess = create_words(p, KNOWN)

        if sorted(guess) == sorted(words):
            # convert guess to a dict with words as keys and digit as value for easier lookup
            found = {guess[i]: i for i in range(0, len(guess))}
            continue
    assert found, 'No guess matches input'

    code = ''
    for word in output:
        code += str(found[word])
    answer += int(code)

pprint(answer)
