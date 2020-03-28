from itertools import cycle, islice
from common.continued_fractions import continued_fraction


def count_digits(n):
    return len(str(n))


def solve(limit=9):
    result = 0
    terms = cycle([2])

    for expansions in range(limit):
        # [1; (2)]
        expansion = continued_fraction(1, islice(terms, expansions))

        if count_digits(expansion.numerator) > count_digits(expansion.denominator):
            result += 1

    return result


if __name__ == "__main__":
    print(solve(1000))
