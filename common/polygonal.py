"""Implementations of the formulas for polygonal numbers
"""


def triangle(n):
    """Return the nth triangle number.

    >>> list(map(triangle, range(1, 6)))
    [1, 3, 6, 10, 15]
    """
    return n * (n + 1) // 2


def square(n):
    """Return the nth square number.

    >>> list(map(square, range(1, 6)))
    [1, 4, 9, 16, 25]
    """
    return n * n


def pentagonal(n):
    """Return the nth pentagonal number.

    >>> list(map(pentagonal, range(1, 6)))
    [1, 5, 12, 22, 35]
    """
    return n * (3*n - 1) // 2


def hexagonal(n):
    """Return the nth hexagonal number.

    >>> list(map(hexagonal, range(1, 6)))
    [1, 6, 15, 28, 45]
    """
    return n * (2*n - 1)


def heptagonal(n):
    """Return the nth heptagonal number.

    >>> list(map(heptagonal, range(1, 6)))
    [1, 7, 18, 34, 55]
    """
    return n * (5*n - 3) // 2


def octagonal(n):
    """Return the nth octagonal number.

    >>> list(map(octagonal, range(1, 6)))
    [1, 8, 21, 40, 65]
    """
    return n * (3*n - 2)
