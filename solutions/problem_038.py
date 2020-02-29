from common.tools import digits
from collections import Counter

PANDIGITAL = Counter(range(1, 10))


def is_pandigital(n):
    return PANDIGITAL == Counter(digits(n))


def concatenated_product(n, up_to):
    result = ""
    for i in range(1, up_to + 1):
        result += str(n * i)

    return result


result = 0
limit = 100_000
scope = 999999999

for x in range(1, limit):
    for up_to in range(1, 10):
        c = int(concatenated_product(x, up_to))

        if c > scope:
            break

        if is_pandigital(c) and c > result:
            result = c

print(result)
