from pprint import pprint
import sys

# TODO this could probably use some cleanup

lines = []
#with open('test.txt') as file:
with open('data.txt') as file:
    for line in file:
        line = line.strip()
        lines.append(line.strip())

MAP = {
    "]": "[",
    "}": "{",
    ")": "(",
    ">": "<"
}

FULL_MAP = {
    "]": "[",
    "}": "{",
    ")": "(",
    ">": "<",
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

SYNTAX_SCORE_MAP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AC_SCORE_MAP = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def isIncomplete(word):
    is_valid, _ = isValid(word + getAutoCorrect(word))

    return is_valid

def isCorrupt(word):
    is_valid, _ = isValid(word)

    if is_valid:
        return False

    return not isIncomplete(word)

# this stack appends until if finds open/close pairs. When it finds one, instead of appending to the
# stack, it pops it off, so that eventually it will only have open/close pairs. The initialization
# of the stack with the '#' is just to prevent an additional check if the stack is empty for the
# last char in a valid word

# example: {()[]}
# i={, stack=#{
# i=(, stack=#{(
# i=), stack=#{, pop=(
# i=[, stack=#{[
# i=], stack=#{, pop=]
# i=}, stack=#, pop=}
# len(stack) == 1 (True, stack is just #)

# returning a tuple here so we can also return the last incorrect character
def isValid(word) -> tuple:
    stack = ['#']

    for i in word:
        if i in MAP.keys():
            if stack.pop() != MAP[i]:
                return (False, i)
        else:
            stack.append(i)

    return (len(stack) == 1, i)

# <{([{{}}[<[[[<>{}]]]>[]]
# <{([{{}}[<[[[<>{}]]]>[]]])}>

# this is similar to isValid, but we are completing the word, so whatever remains on the stack at
# the end of a presumably incomplete word can be reversed/inverted to close everything up
def getAutoCorrect(word) -> tuple:
    stack = ['#']

    for i in word:
        if i in MAP.keys():
            if stack.pop() != MAP[i]:
                break
        else:
            stack.append(i)

    stack.remove('#')
    autocomplete = ''

    # trick to read string in reverse
    for c in stack[::-1]:
        autocomplete += FULL_MAP[c]

    return autocomplete

assert '])}>' == getAutoCorrect('<{([{{}}[<[[[<>{}]]]>[]]')

def calculateAcScore(autocomplete):
    score = 0
    for c in autocomplete:
        score *= 5
        score += AC_SCORE_MAP[c]

    return score

assert calculateAcScore('}}]])})]') == 288957

syntax_score = 0
autocompletes = []
for line in lines:
    if isIncomplete(line):
        autocompletes.append(getAutoCorrect(line))
        continue

    if isCorrupt(line):
        is_valid, last_char = isValid(line)
        assert is_valid == False
        syntax_score += SYNTAX_SCORE_MAP[last_char]

# part 1:
pprint(syntax_score)

ac_scores = []
for word in autocompletes:
    ac_scores.append(calculateAcScore(word))

ac_scores.sort()
mid = len(ac_scores) // 2

# part 2:
pprint(ac_scores[mid])
