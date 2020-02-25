import itertools
from functools import reduce, lru_cache


def factors(n):
    """
    Returns all the factors of n as a set

    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


@lru_cache(maxsize=256)
def proper_divisors(n):
    """The proper divisors of n are its factors other than itself
    """
    return factors(n) - {n}


def sum_of_digits(number):
    return sum([int(x) for x in str(number)])


def nth(iterable, index):
    """Returns the nth index in an iterable
    """
    return next(itertools.islice(iterable, index - 1, None))
