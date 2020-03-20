import itertools
from common.math import factors

LIMIT = 500


def gen_triangle_numbers():
    """
    Generates an infinite sequence of triangle numbers.
    """
    triangle = 0

    for i in itertools.count(1):
        triangle += i
        yield triangle


def solve():
    for triangle in gen_triangle_numbers():
        num_factors = len(factors(triangle))

        if num_factors > LIMIT:
            return triangle


if __name__ == "__main__":
    print(solve())
