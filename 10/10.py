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

"""
this stack appends until if finds open/close pairs. When it finds one, instead of appending to the
stack, it pops it off, so that eventually it will only have open/close pairs. The initialization
of the stack with the '#' is just to prevent an additional check if the stack is empty for the
last char in a valid word

example: {()[]}
i={, stack=#{
i=(, stack=#{(
i=), stack=#{, pop=(
i=[, stack=#{[
i=], stack=#{, pop=]
i=}, stack=#, pop=}
len(stack) == 1 (True, stack is just #)

If we only wanted to check for validity, we would simply: `return len(stack) == 1`.
Instead, we set the `last_wrong_char` for use in "completing" a code that is technically invalid but
actually just incomplete. To check for that incompleteness, we remove the '#', then handle the
incompleteness check. See below.

for the "autocomplete", we can just reverse the rest of the stack at the point of failure to
"complete" the incomplete code.
example:

if code  = <{([{{}}[<[[[<>{}]]]>[]]
complete = <{([{{}}[<[[[<>{}]]]>[]]])}>

see: assert '])}>' == v.autocomplete


"""
class CodeValidator:
    def __init__(self, code: str):
        self.code = code
        self.autocomplete = ''
        self.is_valid = False
        self.last_wrong_char = None
        self.validate()

    def validate(self):
        stack = ['#']

        for i in self.code:
            if i in MAP.keys():
                if stack.pop() != MAP[i]:
                    self.last_wrong_char = i
                    break
            else:
                stack.append(i)

        stack.remove('#')

        if not stack:
            self.is_valid = True
            return

        # trick to read string in reverse
        for c in stack[::-1]:
            self.autocomplete += FULL_MAP[c]

    def isIncomplete(self) -> bool:
        word = CodeValidator(self.code + self.autocomplete)

        return word.is_valid

    def isCorrupt(self) -> bool:
        return not self.is_valid and not self.isIncomplete()

v = CodeValidator('<{([{{}}[<[[[<>{}]]]>[]]')
assert '])}>' == v.autocomplete

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
    validator = CodeValidator(line)
    if validator.isIncomplete():
        autocompletes.append(validator.autocomplete)
        continue

    if validator.isCorrupt():
        syntax_score += SYNTAX_SCORE_MAP[validator.last_wrong_char]

# part 1:
pprint(syntax_score)

ac_scores = []
for word in autocompletes:
    ac_scores.append(calculateAcScore(word))

ac_scores.sort()
mid = len(ac_scores) // 2

# part 2:
pprint(ac_scores[mid])
