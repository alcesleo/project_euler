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

    >>> proper_divisors(10)
    {1, 2, 5}

    >>> proper_divisors(2)
    {1}
    """
    return factors(n) - {n}


def digits(n):
    """Returns a list of the digits in n
    """
    return [int(d) for d in str(n)]


def digits_to_int(d):
    """Returns an int from concatenating a list of its digits
    """
    return int("".join(map(str, d)))


def nth(iterable, index):
    """Returns the nth 1-index in an iterable
    """
    return next(itertools.islice(iterable, index - 1, None))


def is_palindrome(number):
    number = str(number)
    reverse = number[::-1]
    return number == reverse
