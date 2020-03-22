"""Functions for working with individual digits of integers."""

import itertools


def split_digits(n):
    """Return a list of the digits in n.

    >>> split_digits(123)
    [1, 2, 3]
    """
    return [int(d) for d in str(n)]


def join_digits(d):
    """Return an int from concatenating a list of digits.

    >>> join_digits([1, 2, 3])
    123

    >>> join_digits([123, 456])
    123456
    """
    return int("".join(map(str, d)))


def digit_permutations(n):
    """Return all valid permutations of the digits of n.

    There may be fewer than permutations of a string, as leading zeros yield non-valid integer permutations.

    >>> digit_permutations(123)
    {321, 132, 231, 213, 312, 123}

    >>> digit_permutations(100)
    {100}
    """
    return set(map(join_digits, filter(lambda p: p[0] != 0, itertools.permutations(split_digits(n)))))
