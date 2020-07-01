from itertools import takewhile
from common.primes import gen_primes


def solve(limit):
    """Returns the sum of all primes below limit.

    >>> solve(10)
    17
    """
    return sum(takewhile(lambda p: p < limit, gen_primes()))


if __name__ == "__main__":
    print(solve(2_000_000))
