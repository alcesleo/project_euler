from math import prod
from itertools import count
from common.digits import split_digits
from common.tools import nth


def gen_champernownes_decimals():
    for i in count(1):
        for d in split_digits(i):
            yield d


def nth_champernowne_decimal(index):
    return nth(gen_champernownes_decimals(), index)


def solve():
    return prod(
        map(nth_champernowne_decimal, [1, 100, 1000, 10_000, 100_000, 1_000_000]))


if __name__ == "__main__":
    print(solve())
