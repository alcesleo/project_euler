"""
To minimize n/phi(n), we need to maximize phi(n).

To restrict the search space, search only products of two primes around the square root of the limit.

https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""

from math import sqrt, prod, inf
from itertools import combinations

from common.primes import gen_primes
from common.tools import ibetween
from common.math import phi
from common.logging import info


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def solve(limit, search_delta=0.3):
    lower = int(sqrt(limit) * (1 - search_delta))
    upper = int(sqrt(limit) * (1 + search_delta))
    primes = list(ibetween(gen_primes(), lower, upper))

    info(f"Searching using prime factors {lower} < p < {upper}")

    result_n, result_q = None, inf

    for factors in combinations(primes, 2):
        n = prod(factors)

        if n > limit:
            continue

        phi_n = phi(n)

        if is_permutation(n, phi_n):
            q = n / phi_n

            if q < result_q:
                result_n, result_q = n, q

            info(
                f"n = {n}\tphi(n) = {phi_n}\tn/phi(n) = {q}")

    return result_n


if __name__ == "__main__":
    print(solve(10 ** 7))
