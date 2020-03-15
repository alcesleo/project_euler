"""
Only a single fraction will be relevant for every single denominator -
the one with a numerator bringing it as close below 3/7 as possible.
"""

from fractions import Fraction

TARGET = Fraction(3, 7)


def solve(limit=8):
    closest_fraction = 0

    for d in range(1, limit + 1):
        n = int(d * TARGET)
        f = Fraction(n, d)

        if f > closest_fraction and f < TARGET:
            closest_fraction = f

    return closest_fraction.numerator


if __name__ == "__main__":
    result = solve(1_000_000)
    print(result)
