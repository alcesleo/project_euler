from fractions import Fraction
from functools import lru_cache
from common.tools import split_digits

LIMIT = 1000


def expand_root_two(iterations):
    """Expands the square root of two by a number of iterations, equivalent to the following:

    1 + Fraction(1, 2)
    1 + Fraction(1, 2 + Fraction(1, 2))
    1 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2)))
    1 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2))))

    >>> expand_root_two(0)
    Fraction(3, 2)

    >>> expand_root_two(1)
    Fraction(7, 5)

    >>> expand_root_two(2)
    Fraction(17, 12)

    >>> expand_root_two(3)
    Fraction(41, 29)
    """
    return 1 + Fraction(1, denominator(iterations))


@lru_cache(maxsize=1)
def denominator(iterations):
    if iterations == 0:
        return 2

    return 2 + Fraction(1, denominator(iterations - 1))


def count_digits(n):
    return len(split_digits(n))


def solve():
    result = 0

    for i in range(LIMIT):
        expansion = expand_root_two(i)

        if count_digits(expansion.numerator) > count_digits(expansion.denominator):
            result += 1

    return result


print(solve())
