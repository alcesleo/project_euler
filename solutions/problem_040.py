from functools import reduce
from operator import mul
from itertools import count
from common.tools import split_digits, nth


def gen_champernownes_decimals():
    for i in count(1):
        for d in split_digits(i):
            yield d


def nth_champernowne_decimal(index):
    return nth(gen_champernownes_decimals(), index)


result = reduce(
    mul, map(nth_champernowne_decimal, [1, 100, 1000, 10_000, 100_000, 1_000_000]))

print(result)
