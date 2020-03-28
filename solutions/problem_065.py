"""
https://en.wikipedia.org/wiki/E_(mathematical_constant)
https://en.wikipedia.org/wiki/Continued_fraction
"""


from itertools import count, islice
from common.digits import sum_digits

from common.continued_fractions import continued_fraction


def gen_terms_e():
    """Yields the terms of the continued fraction for e.

    https://oeis.org/A003417

    >>> list(islice(gen_terms_e(), 20))
    [1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14]
    """
    for i in count():
        if i % 3 == 1:
            yield 2 * (1 + i//3)
        else:
            yield 1


def solve(target=10):
    # [2; 1, 2, 1, 1, 4, 1, 1, ...]
    terms = islice(gen_terms_e(), target - 1)
    convergent = continued_fraction(2, terms)

    return sum_digits(convergent.numerator)


if __name__ == "__main__":
    print(solve(100))
