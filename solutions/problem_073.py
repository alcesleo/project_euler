"""
If n and d are relatively prime, they produce a properly reduced fraction,
this is much faster than creating a bunch of Fraction objects and keeping a set of the ones you already tried.

Much like 71 you can get away with only checking the numerators that produce fractions between the limits.
"""
from math import gcd
from fractions import Fraction

UPPER = Fraction(1, 2)
LOWER = Fraction(1, 3)


def relatively_prime(a, b):
    return gcd(a, b) == 1


def solve(limit=8):
    result = 0

    for d in range(3, limit + 1):
        lower = int(d * LOWER) + 1
        upper = int(d * UPPER) + 1

        for n in range(lower, upper):
            if relatively_prime(n, d):
                result += 1

    return result


def verify(limit=8):
    """Verify that the solve() method gives the same result as this more obviously correct but slow method.
    """
    result = set()

    for d in range(2, limit + 1):
        for n in range(1, d):
            f = Fraction(n, d)

            if f > LOWER and f < UPPER:
                result.add(f)

    return len(result)


if __name__ == "__main__":
    print(solve(12_000))
