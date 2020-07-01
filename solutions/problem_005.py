from functools import reduce
from math import gcd


def lcm(a, b):
    """Returns the lowest common multiple of a and b."""
    return a * b // gcd(a, b)


def lcms(*numbers):
    """Returns the lowest common multiple among all its arguments."""
    return reduce(lcm, numbers)


def solve(limit):
    return lcms(*range(1, limit))


if __name__ == "__main__":
    print(solve(20))
