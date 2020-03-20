"""
The amount of fractions for each n is the Euler's Totient
"""

from common.math import phi


def solve(limit=8):
    result = 0
    for n in range(2, limit + 1):
        result += phi(n)

    return result


def verify(limit=8):
    """Verify that the solve() method gives the same result as this more obviously correct but slow method.
    """
    result = set()

    for d in range(2, limit + 1):
        for n in range(1, d):
            result.add(Fraction(n, d))

    return len(result)


if __name__ == "__main__":
    result = solve(1_000_000)
    print(result)
