from itertools import combinations_with_replacement
from common.math import proper_divisors
from common.logging import info

LIMIT = 28123


def is_abundant(n):
    return sum(proper_divisors(n)) > n


def gen_abundant_numbers(up_to):
    abundant_numbers = set()

    for i in range(1, up_to):
        if is_abundant(i):
            abundant_numbers.add(i)

    return abundant_numbers


def gen_sums_of_abundant_numbers(up_to):
    abundant_numbers = gen_abundant_numbers(up_to)
    sums = set()

    for a, b in combinations_with_replacement(abundant_numbers, 2):
        if a + b < up_to:
            sums.add(a + b)

    return sums


def solve():
    sums_of_abundant_numbers = gen_sums_of_abundant_numbers(LIMIT)
    all_numbers = set(range(1, LIMIT))
    not_sums_of_abundant_numbers = all_numbers - sums_of_abundant_numbers

    return sum(not_sums_of_abundant_numbers)

if __name__ == "__main__":
    print(solve())
