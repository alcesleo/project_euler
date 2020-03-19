from functools import lru_cache
from common.tools import split_digits


def next_number(n):
    """Returns the next number in the number chain

    >>> next_number(44)
    32

    >>> next_number(89)
    145
    """
    return sum(map(lambda d: d**2, split_digits(n)))


@lru_cache(maxsize=1_000_000)
def last_number(n):
    """Returns the number the chain starting with n terminates in, either 89 or 1
    """
    if n != 1 and n != 89:
        return last_number(next_number(n))

    return n


def solve(limit):
    result = 0

    for i in range(1, limit):
        if last_number(i) == 89:
            result += 1

    return result


if __name__ == "__main__":
    print(solve(10_000_000))
