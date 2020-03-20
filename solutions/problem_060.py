from itertools import islice, takewhile, combinations
from collections import defaultdict
import math

from common.primes import gen_primes, is_prime
from common.digits import join_digits


def concatenates_to_prime(a, b):
    """Returns whether both ab and ba are prime

    >>> concatenates_to_prime(109, 673)
    True
    """
    return is_prime(join_digits((a, b))) and is_prime(join_digits((b, a)))


def prime_pairs(primes):
    """Returns a dict of primes mapped to a set of primes with which they form a pair.

    >>> primes = list(islice(gen_primes(), 10))
    >>> prime_pairs(primes)
    defaultdict(<class 'set'>, {3: {17, 11, 7}, 7: {19, 3}, 11: {3, 23}, 17: {3}, 19: {13, 7}, 23: {11}, 13: {19}})
    """
    prime_pairs = defaultdict(set)

    for a, b in combinations(primes, 2):
        if concatenates_to_prime(a, b):
            prime_pairs[a].add(b)
            prime_pairs[b].add(a)

    return prime_pairs


def make_groups(group, pairs, group_size, prime_pairs):
    """Returns a list of groups with which the group can be expanded using its pairs to form a group of at least a specified size.

    >>> prime_pairs = prime_pairs(list(islice(gen_primes(), 20)))
    >>> make_groups(frozenset([3]), {67, 37, 7, 73, 11, 17, 59, 31}, group_size=3, prime_pairs=prime_pairs)
    {frozenset({67, 3, 37})}
    """
    result = set()

    for pair in pairs:
        new_group = group | {pair}
        new_pairs = pairs & prime_pairs[pair]

        # Pairs exhausted, filter out too small groups
        if new_pairs == set() and len(new_group) == group_size:
            result.add(new_group)
        else:
            result |= make_groups(new_group, new_pairs,
                                  group_size=group_size, prime_pairs=prime_pairs)

    return result


def solve(group_size=4, limit=1000):
    primes = list(takewhile(lambda n: n < limit, gen_primes()))
    pairs = prime_pairs(primes)
    lowest_sum = math.inf

    for prime in primes:
        groups = make_groups(
            frozenset([prime]), pairs[prime], group_size, pairs)

        for group in groups:
            if sum(group) < lowest_sum:
                lowest_sum = sum(group)

    return lowest_sum


if __name__ == "__main__":
    print(solve(5, 10_000))
