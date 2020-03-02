import itertools


def triangle(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def to_generator(fn):
    for i in itertools.count(1):
        yield(fn(i))


def in_sequence_factory(generator):
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
    is_pentagonal = in_sequence_factory(to_generator(pentagonal))
    is_hexagonal = in_sequence_factory(to_generator(hexagonal))

    for i in itertools.count(START):
        t = triangle(i)

        if is_pentagonal(t) and is_hexagonal(t):
            return t


print(solve())
