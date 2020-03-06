from common.primes import gen_primes, is_prime
from common.tools import digits, concatenate_digits

EXCLUDE = {2, 3, 5, 7}


def truncations(n):
    """
    Returns all possible truncations of n

    truncations(3797) # => {97, 3, 37, 7, 3797, 379, 797}
    """

    d = digits(n)
    result = set([n])

    for i in range(1, len(d)):
        result.add(concatenate_digits(d[i:]))
        result.add(concatenate_digits(d[:i]))

    return result


TARGET = 11

truncatable_primes = set()

for p in gen_primes():
    if len(truncatable_primes) == TARGET:
        break

    if all(map(is_prime, truncations(p))) and p not in EXCLUDE:
        truncatable_primes.add(p)

print(sum(truncatable_primes))
