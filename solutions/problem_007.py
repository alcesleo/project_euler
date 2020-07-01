from common.primes import gen_primes
from common.tools import nth


def solve(target):
    return nth(gen_primes(), target)


if __name__ == "__main__":
    print(solve(10_001))
