from common.tools import factors
from common.primes import is_prime
import decimal

# https://en.wikipedia.org/wiki/Repeating_decimal
# https://www.youtube.com/watch?v=rVhU8Vyhz7c

# The number of recurring decimals is always less than the denominator

LIMIT = 1000
NUMERATOR = 1

context = decimal.Context(prec=LIMIT * 2)
decimal.setcontext(context)


def prime_factors(n):
    return set(filter(is_prime, factors(n)))


def is_recurring(denominator):
    """
    If the prime factors of the denominator is 2, 5 or both, the decimal is terminating.
    """
    return not {2, 5}.issuperset(prime_factors(denominator))


def decimals(denominator):
    """Returns the decimals of NUMERATOR / denominator with the 0. and last rounded number stripped
    """
    return str(NUMERATOR / decimal.Decimal(denominator))[2:-1]


def recurring_cycle(denominator):
    """Returns the length of the recurring cycle of decimals
    """
    if not is_recurring(denominator):
        return 0

    decimals_reversed = decimals(denominator)[::-1]

    for i in range(1, len(decimals_reversed) // 2 + 1):
        if decimals_reversed[0:i] == decimals_reversed[i:i*2]:
            return i

    # not repeating?
    return 0


def solve():
    longest_recurring_cycle = 0
    longest_recurring_cycle_denominator = 0

    for d in range(1, LIMIT + 1):
        recurring_cycle_length = recurring_cycle(d)
        if recurring_cycle_length > longest_recurring_cycle:
            longest_recurring_cycle = recurring_cycle_length
            longest_recurring_cycle_denominator = d

    return longest_recurring_cycle_denominator


print(solve())