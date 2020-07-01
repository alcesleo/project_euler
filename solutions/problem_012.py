import itertools
from common.math import factors


def gen_triangle_numbers():
    """
    Generates an infinite sequence of triangle numbers.
    """
    triangle = 0

    for i in itertools.count(1):
        triangle += i
        yield triangle


def solve(limit):
    """Returns the first number to have over _limit_ divisors.

    >>> solve(5)
    28
    """
    for triangle in gen_triangle_numbers():
        num_factors = len(factors(triangle))

        if num_factors > limit:
            return triangle


if __name__ == "__main__":
    print(solve(500))
