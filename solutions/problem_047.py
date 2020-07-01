from itertools import count
from functools import reduce, lru_cache
from collections import Counter
from operator import __or__
from common.tools import gen_window


@lru_cache(maxsize=8)
def prime_factors(n):
    """Returns prime factors and their exponents of n as a Counter object

    >>> prime_factors(14)
    Counter({2: 1, 7: 1})

    >>> prime_factors(644)
    Counter({2: 2, 7: 1, 23: 1})
    """
    result = Counter()

    # Add the 2's to the result until the number is odd
    while n % 2 == 0:
        n //= 2
        result.update([2])

    # Add odd prime factors up to sqrt(n)
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        while n % i == 0:
            n //= i
            result.update([i])

    # If n is not yet below 2, it is also a factor
    if n > 2:
        result.update([n])

    return result


def exponentiate_counter(counter):
    """Returns a set of all the keys in counter to their values' power

    >>> exponentiate_counter(Counter([2, 2, 3, 5]))
    {3, 4, 5}
    """
    result = set()

    for p, e in counter.most_common():
        result.add(p ** e)

    return result


def none_intersect(sets):
    """Returns True if none of the given set intersect with any other

    >>> none_intersect([{2, 3}, {3, 4}])
    False

    none_intersect([{2, 7}, {3, 5}])
    True
    """

    # Sum of the individual lengths equal to the sum of the union of all sets
    return len(reduce(__or__, sets)) == sum(map(len, sets))


def solve(target):
    for window in gen_window(count(1), target):
        prime_factor_window = list(map(prime_factors, window))

        all_target_factors = all(
            map(lambda s: len(s) == target, prime_factor_window))

        no_common_factors = none_intersect(
            list(map(exponentiate_counter, prime_factor_window)))

        if all_target_factors and no_common_factors:
            return window[0]


if __name__ == "__main__":
    print(solve(4))
