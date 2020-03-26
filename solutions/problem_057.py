from fractions import Fraction
from functools import lru_cache
from common.digits import split_digits

LIMIT = 1000


def converge(precision):
    """Expands the square root of two by a number of iterations, equivalent to the following:

    1 + Fraction(1, 2)
    1 + Fraction(1, 2 + Fraction(1, 2))
    1 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2)))
    1 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2 + Fraction(1, 2))))

    >>> converge(0)
    Fraction(3, 2)

    >>> converge(1)
    Fraction(7, 5)

    >>> converge(2)
    Fraction(17, 12)

    >>> converge(3)
    Fraction(41, 29)
    """
    return 1 + Fraction(1, denominator(precision))


@lru_cache(maxsize=1)
def denominator(precision):
    if precision == 0:
        return 2

    return 2 + Fraction(1, denominator(precision - 1))


def count_digits(n):
    return len(split_digits(n))


def solve():
    result = 0

    for precision in range(LIMIT):
        expansion = converge(precision)

        if count_digits(expansion.numerator) > count_digits(expansion.denominator):
            result += 1

    return result


if __name__ == "__main__":
    print(solve())
