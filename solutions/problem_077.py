from common.math import partitions
from common.primes import gen_primes


def solve(target=5):
    n = 0
    ways = 0
    prime = gen_primes()
    primes = (next(prime),)

    while ways < target:
        n += 1

        while primes[0] < n:
            primes = (next(prime),) + primes

        ways = partitions(n, primes)

    return n


if __name__ == "__main__":
    print(solve(5_000))
