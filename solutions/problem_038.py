from collections import Counter
from common.digits import split_digits
from common.logging import info

PANDIGITAL = Counter(range(1, 10))


def is_pandigital(n):
    return PANDIGITAL == Counter(split_digits(n))


def concatenated_product(n, up_to):
    result = ""
    for i in range(1, up_to + 1):
        result += str(n * i)

    return result


def solve():
    largest_pandigital = 0
    limit = 100_000
    scope = 999999999

    for x in range(1, limit):
        for up_to in range(1, 10):
            c = int(concatenated_product(x, up_to))

            if c > scope:
                break

            if is_pandigital(c) and c > largest_pandigital:
                info(f"{c}, n={up_to}")
                largest_pandigital = c

    return largest_pandigital


if __name__ == "__main__":
    print(solve())
