from math import factorial
from functools import lru_cache
from common.digits import split_digits


@lru_cache(maxsize=1_000_000)
def digit_factorial(n):
    return sum(map(factorial, split_digits(n)))


def len_factorial_chain(n):
    """Returns the number of terms of a chain starting with n.

    >>> len_factorial_chain(169)
    3

    >>> len_factorial_chain(69)
    5
    """
    visited = set()

    while n not in visited:
        visited.add(n)
        n = digit_factorial(n)

    return len(visited)


def solve(target, limit):
    result = 0

    for n in range(limit):
        if len_factorial_chain(n) == target:
            result += 1

    return result


if __name__ == "__main__":
    print(solve(60, 1_000_000))
