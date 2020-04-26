"""General tools
"""

import itertools
import os


def nth(iterable, index):
    """Return the nth 1-index in an iterable."""
    return next(itertools.islice(iterable, index - 1, None))


def ibetween(iterable, lower, upper):
    """Return the values between a lower and upper bound in an iterable.

    Much like itertools.islice, but with values rather than indexes

    >>> list(ibetween(itertools.count(), 5, 10))
    [5, 6, 7, 8, 9]
    """
    return itertools.takewhile(
        lambda p: p < upper,
        itertools.dropwhile(
            lambda p: p < lower,
            iterable))


def to_generator(fn, start=1):
    """Given a function fn that takes an int n, returns a generator that counts up fn of n."""
    for i in itertools.count(start):
        yield(fn(i))
