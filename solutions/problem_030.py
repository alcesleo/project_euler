from common.digits import split_digits
from common.logging import info, debug


def sum_of_digits_raised(n, power):
    return sum([x ** power for x in split_digits(n)])


def solve(power, limit=100_000):
    """
    >>> solve(4)
    19316
    """
    result = 0

    for n in range(2, limit):
        if n == sum_of_digits_raised(n, power):
            info(f"{n} = {' + '.join(map(lambda d: f'{d}^{power}', list(str(n))))}")
            result += n

    return result

if __name__ == "__main__":
    limit = 500_000  # Found by trial and error
    print(solve(5, limit))
