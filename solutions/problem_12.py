import itertools
from functools import reduce
from common.factors import factors

LIMIT = 500


def gen_triangle_numbers():
    """
    Generates an infinite sequence of triangle numbers.
    """
    triangle = 0

    for i in itertools.count(1):
        triangle += i
        yield triangle


for triangle in gen_triangle_numbers():
    num_factors = len(factors(triangle))

    if num_factors > LIMIT:
        print(triangle)
        break
