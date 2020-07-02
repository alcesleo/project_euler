from itertools import dropwhile
from common.primes import gen_primes, is_prime
from common.digits import split_digits, join_digits
from common.logging import info

EXCLUDE = {2, 3, 5, 7}


def truncations(n):
    """
    Returns all possible truncations of n.

    >>> truncations(3797)
    {97, 3, 37, 7, 3797, 379, 797}
    """
    d = split_digits(n)
    result = set([n])

    for i in range(1, len(d)):
        result.add(join_digits(d[i:]))
        result.add(join_digits(d[:i]))

    return result


def solve(target):
    truncatable_primes = set()
    primes = dropwhile(lambda p: p in EXCLUDE, gen_primes())

    for p in primes:
        if len(truncatable_primes) == target:
            break

        truncations_p = truncations(p)
        if all(map(is_prime, truncations_p)):
            info(f"{p} = {truncations_p}")
            truncatable_primes.add(p)

    return sum(truncatable_primes)

if __name__ == "__main__":
    print(solve(11))
