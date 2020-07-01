from common.digits import sum_digits


def solve(exponent):
    """
    >>> solve(15)
    26
    """
    return sum_digits(2 ** exponent)


if __name__ == "__main__":
    print(solve(1000))
