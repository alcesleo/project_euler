"""After just finishing 79 which had a difficulty of 5/100, feeling like
it should have been more of a 15-20/100; this one feels exactly the opposite.

We are getting away with three nested loops by simply setting the limit to the square
root and not repeating operations within the loops, and it runs in ~1s.
"""

from itertools import takewhile
from math import sqrt
from common.primes import gen_primes
from common.logging import info


def solve(limit=50):
    numbers = set()
    primes = list(takewhile(lambda p: p < sqrt(limit), gen_primes()))

    for a in primes:
        a2 = a**2

        for b in primes:
            b3 = b**3

            ab = a2 + b3

            for c in primes:
                c4 = c**4
                abc = ab + c4

                if abc >= limit:
                    break

                info(f"{abc} = {a}^2 + {b}^3 + {c}^4")
                numbers.add(abc)

    return len(numbers)


if __name__ == "__main__":
    print(solve(50_000_000))
