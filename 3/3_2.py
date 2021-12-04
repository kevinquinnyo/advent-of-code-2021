#!/usr/bin/python3
from pprint import pprint
from enum import Enum
import sys

# multiplying the oxygen generator rating by the CO2 scrubber rating.
# bit criteria

#    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
#    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
#

# cache the data in case we call it more than once?
class DataFetcher:
    items = []
    def get_data(self) -> list:
        if not self.items:
            for line in self.fetch_data():
                self.items.append(line)

        return self.items

    def fetch_data(self):
        with open('data.txt') as file:
            for line in file:
                yield list(line.rstrip())

class Popularity:
    zero_count = 0
    one_count = 0

    def __init__(self, data: list):
        self.data = [int(n) for n in data]
        self.parse()

    def parse(self):
        self.zero_count = self.data.count(0)
        self.one_count = len(self.data) - self.zero_count

    def get_most_common(self, tiebreaker: int) -> int:
        if self.zero_count == self.one_count:
            return tiebreaker

        return 0 if self.zero_count > self.one_count else 1

    def get_least_common(self, tiebreaker: int) -> int:
        if self.zero_count == self.one_count:
            return tiebreaker

        return 0 if self.zero_count < self.one_count else 1

class Gas(Enum):
    O2 = 1
    CO2 = 2

def binary_list_to_int(l: list) -> int:
    return int(''.join(l), base=2)

'''
returns string representation of binary
'''
def get_rating(data: list, gas: Gas, pos: int) -> list:
    if (len(data) == 1):
        return list(data)[0]

    col = []
    for i, line in enumerate(data):
        col.append(line[pos])

    popularity = Popularity(col)
    if gas == Gas.O2:
        search = popularity.get_most_common(1)
    else:
        search = popularity.get_least_common(0)

    next_data = []
    for i, line in enumerate(data):
        if int(line[pos]) == search:
            next_data.append(line)

    pos += 1

    return get_rating(next_data, gas, pos)

fetcher = DataFetcher()
data = fetcher.get_data()

o2 = binary_list_to_int(get_rating(data, Gas.O2, 0))
co2 = binary_list_to_int(get_rating(data, Gas.CO2, 0))

pprint(o2 * co2)
