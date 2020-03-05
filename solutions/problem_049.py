from itertools import takewhile, dropwhile, permutations, combinations
from common.primes import gen_primes
from common.tools import digits, digits_to_int


def digit_permutations(n):
    """Returns all permutations of digits of n

    >>> digit_permutations(123)
    {321, 132, 231, 213, 312, 123}
    """
    return set(map(digits_to_int, permutations(digits(n))))


def difference_list(l):
    """Returns a list of the sequence of differences in a list

    >>> difference_list([2, 8, 14, 16])
    [6, 6, 2]
    """
    return [b - a for a, b in zip(l[:-1], l[1:])]


def equidistant(l):
    """Returns whether all elements in l have the same difference from each other

    >>> equidistant([1487, 4817, 8147])
    True

    >>> equidistant([2, 4, 6, 9])
    False
    """
    return len(set(difference_list(l))) == 1


LOWER = 1000
UPPER = 10000
EXCLUDE = 148748178147


def solve():
    four_digit_primes = set(takewhile(lambda p: p < UPPER,
                                      dropwhile(lambda p: p < LOWER, gen_primes())))

    for prime in four_digit_primes:
        prime_permutations = digit_permutations(prime) & four_digit_primes
        terms_of_three = combinations(prime_permutations, 3)

        for terms in terms_of_three:
            if equidistant(terms):
                result = digits_to_int(terms)
                if result != EXCLUDE:
                    return result


print(solve())
