from itertools import count, cycle, takewhile
from common.polygonal import pentagonal
from common.logging import info


def gen_generalized_pentagonals():
    """Generates the series of generalized pentagonal numbers.

    This is given by inputing the sequence 1, -1, 2, -2, 3, -3, ... to the pentagonal function.

    https://oeis.org/A001318
    """
    for i in count(1):
        yield pentagonal(i)
        yield pentagonal(-i)


def gen_partitions():
    """Generates the partition sequence.

    This uses the Pentagonal number theorem:

    > The identity implies a marvelous recurrence for calculating p(n), the number of partitions of n:
    > p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + ...
    >
    > [...] the series will eventually become zeroes, enabling discrete calculation.

    * The sign follows the pattern --++
    * The exponent coefficients are the generalized pentagonals

    - https://en.wikipedia.org/wiki/Partition_(number_theory)
    - https://en.wikipedia.org/wiki/Pentagonal_number_theorem
    - https://oeis.org/A000041
    """
    partitions = [1]
    signs = [1, 1, -1, -1]

    for n in count():
        partitions.append(0)

        pentagonals = takewhile(lambda penta: penta <= n,
                                gen_generalized_pentagonals())

        for sign, penta in zip(cycle(signs), pentagonals):
            partitions[n] += sign * partitions[n - penta]

        if (partitions[n] == 0):
            break

        info(f"p({n})={partitions[n]}")
        yield partitions[n]


def solve(target):
    for n, p in enumerate(gen_partitions()):
        if p % target == 0:
            return n


if __name__ == "__main__":
    print(solve(1_000_000))
