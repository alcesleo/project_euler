from collections import defaultdict

from common.primes import gen_primes, is_prime

TARGET = 8


def solve():
    masks = defaultdict(set)

    for prime in gen_primes():
        digits = str(prime)

        for masked_digit in set(digits):
            masked = digits.replace(masked_digit, "x")

            for replaced_digit in range(10):
                candidate = int(masked.replace("x", str(replaced_digit)))

                # Discard leading zeros
                if len(str(candidate)) != len(masked):
                    continue

                if is_prime(candidate):
                    masks[masked].add(candidate)

            if len(masks[masked]) >= TARGET:
                return min(masks[masked])


print(solve())
