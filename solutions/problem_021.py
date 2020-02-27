from common.tools import proper_divisors


def is_amicable(a, b):
    return a != b and sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a


LIMIT = 10_000

result = 0
for a in range(1, LIMIT):
    for b in range(a, LIMIT):
        if is_amicable(a, b):
            result += a + b

print(result)
