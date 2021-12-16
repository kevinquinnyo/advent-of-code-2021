from pprint import pprint
import sys
from collections import defaultdict, Counter
from enum import Enum


template = None
imap = {}

with open('test.txt') as file:
#with open('data.txt') as file:
    for line in file:
        line = line.rstrip()
        if not template:
            template = list(line)
            continue
        if not line:
            continue
        between, insert = line.split(' -> ')
        imap[between] = insert

uniq = set()
for k, v in imap.items():
    uniq.add(v)
    for c in k:
        uniq.add(c)

# initialize a frequency map with 0's for every unique element
freq = {elem: 0 for elem in uniq}

# this does not scale
def poly(template: str) -> str:
    # we add a string termination char on the end just to allow appending the final char
    template = list(template)
    template.append('#')
    result = ''
    left = ''

    while template:
        right = template.pop(0)
        result += left
        key = left + right
        if key in imap:
            result += imap[key]
        left = right

    return result

result = template
for i in range(0, 10):
    result = poly(result)

for c in uniq:
    freq[c] = result.count(c)

# part 1
pprint(max(freq.values()) - min(freq.values()))

# part 2 below
# I could delete part 1, but it's nice to keep so we can see how the problem was approached before
# I knew it wouldn't scale

# The trick here is that since we are always taking a pair that includes the *inserted* letter, the
# inserted letter is shared among the left and right pairs.
# This means we can simply increment every new pair created, e.g. AB -> C: (AC, CB), then just
# increment every first letter we find in the pair_count. We have to increment the last character
# afterwards which will not be changed from the original string because we never add anything in
# this algorithm. It only adds chars to the middle.
# We could also choose to count the second letter of each pair, then increment the first letter of
# the template. Or we could count both the first and second, then divide it all by 2 (i think?)

pair_count = Counter()
for i in range(len(template) - 1):
    pair = template[i] + template[i + 1]
    pair_count[pair] += 1

for i in range(40):
    # init new inner pair count for every iteration
    inner_pair_count = Counter()
    for k in pair_count:
        tmp = pair_count[k]
        left = k[0] + imap[k]
        right = imap[k] + k[1]

        #pprint({'k': k, 'tmp': tmp, 'left': left, 'right': right})
        inner_pair_count[left] += tmp
        inner_pair_count[right] += tmp

    pair_count = inner_pair_count

char_count = Counter()
for k in pair_count:
    first = k[0]
    #pprint({'k': k, 'first': first, 'count': pair_count[k], 'char_count[k[0]]': char_count[k[0]]})
    char_count[first] += pair_count[k]

# increment last char which will be the same as the original last char
last = template[-1]
char_count[last] += 1

pprint(max(char_count.values()) - min(char_count.values()))
