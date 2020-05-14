"""
This one turned out to be way easier than I expected, it has a 40% difficulty rating
which is higher than I've done before, and it uses the combinations function **on the
result of a previous call of the combinations function**. I was sure this was going
to be one of those "oh now I understand the problem but this clearly will take years"-
implementations, but it runs way under a second, there are actually not many combinations
to check.
"""

from itertools import combinations
from common.digits import join_digits
from common.logging import info

SQUARES = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5),
           (3, 6), (4, 9), (6, 4), (8, 1)]


def flippable(cube):
    if 9 in cube:
        return cube | {6}

    if 6 in cube:
        return cube | {9}

    return cube


def solve():
    digits = tuple(range(10))

    cubes = combinations(digits, 6)
    cubes = map(set, cubes)
    cubes = map(flippable, cubes)

    pairs = combinations(cubes, 2)

    result = 0

    for c1, c2 in pairs:
        for s1, s2 in SQUARES:
            if not ((s1 in c1 and s2 in c2) or
                    (s2 in c1 and s1 in c2)):
                break
        else:
            result += 1
            info(f"{c1}, {c2}")

    return result


if __name__ == "__main__":
    print(solve())
