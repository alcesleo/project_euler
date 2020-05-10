import itertools

from common.polygonal import triangle, pentagonal, hexagonal
from common.tools import sequence


def in_sequence_factory(generator):
    """Returns a function given a generator which is assumed to return increasing numbers.

    The function returns whether n is a member of the generator,
    generating only as many numbers from the generator needed to answer the question.
    """
    found = set()
    highest = 0

    def in_sequence_fn(n):
        nonlocal highest

        while n > highest:
            highest = next(generator)
            found.add(highest)

        return n in found

    return in_sequence_fn


START = 286


def solve():
    is_pentagonal = in_sequence_factory(sequence(pentagonal))
    is_hexagonal = in_sequence_factory(sequence(hexagonal))

    for i in itertools.count(START):
        t = triangle(i)

        if is_pentagonal(t) and is_hexagonal(t):
            return t


print(solve())
