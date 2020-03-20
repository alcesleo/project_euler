from common.digits import split_digits, join_digits
from common.math import is_palindrome

LIMIT = 10_000


def reverse_digits(n):
    """
    >>> reverse_digits(1292)
    2921
    """
    return join_digits(reversed(split_digits(n)))


def is_lychrel(n, limit=50):
    for _ in range(limit):
        n = n + reverse_digits(n)

        if is_palindrome(n):
            return False

    return True


print(sum(map(is_lychrel, range(LIMIT))))
