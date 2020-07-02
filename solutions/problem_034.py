from math import factorial
from common.digits import split_digits
from common.logging import info


def digit_factorial(n):
    return sum(map(factorial, split_digits(n)))


def solve():
    result = 0
    limit = 50_000 # Found by trial and error

    for n in range(3, limit):
        if n == digit_factorial(n):
            info(f"%s = {n}", " + ".join(map(lambda d: d + "!", (str(n)))))
            result += n

    return result


if __name__ == "__main__":
    print(solve())
