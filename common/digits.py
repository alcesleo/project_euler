"""Functions for working with individual digits of integers
"""
import itertools


def split_digits(n):
    """Returns a list of the digits in n

    >>> split_digits(123)
    [1, 2, 3]
    """
    return [int(d) for d in str(n)]


def join_digits(d):
    """Returns an int from concatenating a list of digits

    >>> join_digits([1, 2, 3])
    123

    >>> join_digits([123, 456])
    123456
    """
    return int("".join(map(str, d)))


def digit_permutations(n):
    """Returns all valid permutations of the digits of n,
    these may be fewer than permutations of a string as leading zeros yield non-valid permutations.

    >>> digit_permutations(123)
    {321, 132, 231, 213, 312, 123}

    >>> digit_permutations(100)
    {100}
    """
    return set(map(join_digits, filter(lambda p: p[0] != 0, itertools.permutations(split_digits(n)))))
