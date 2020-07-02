from itertools import takewhile
from collections import deque
from common.digits import split_digits, join_digits
from common.primes import gen_primes, is_prime
from common.logging import info


def rotations(n):
    d = deque(split_digits(n))
    result = []

    for i in range(len(d)):
        result.append(join_digits(d))
        d.rotate()

    return result


def solve(limit):
    """Returns the numbers of circular primes below limit.

    >>> solve(100)
    13
    """
    primes = takewhile(lambda n: n < limit, gen_primes())
    count = 0

    for p in primes:
        if all(map(is_prime, rotations(p))):
            info(p)
            count += 1

    return count


if __name__ == "__main__":
    print(solve(1_000_000))
