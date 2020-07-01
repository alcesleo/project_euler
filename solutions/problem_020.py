import math
from common.digits import sum_digits


def solve(target):
    """
    >>> solve(10)
    27
    """
    return sum_digits(math.factorial(target))


if __name__ == "__main__":
    print(solve(100))
