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


def sequence(fn, start=1):
    """Given a function fn that takes an int n, returns a generator that counts up fn of n."""
    for i in itertools.count(start):
        yield(fn(i))


def slice_grid(grid, row=0, col=0, num_items=None, hstep=0, vstep=0):
    """Take a one-dimensional slice of a two-dimensional grid.

    >>> grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    >>> slice_grid(grid, col=1, vstep=1)
    [2, 5, 8]

    >>> slice_grid(grid, hstep=1, vstep=1)
    [1, 5, 9]
    """
    result = []

    while num_items == None or len(result) < num_items:
        if row >= len(grid) or col >= len(grid[row]):
            return result

        result.append(grid[row][col])
        row += vstep
        col += hstep

    return result
