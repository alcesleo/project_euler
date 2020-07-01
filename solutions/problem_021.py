from common.math import proper_divisors
from common.logging import info

def solve(limit):
    divisor_sum = {}
    for n in range(limit):
        divisor_sum[n] = sum(proper_divisors(n))

    result = 0
    for a in range(1, limit):
        for b in range(a + 1, limit):
            if divisor_sum[a] == b and divisor_sum[b] == a:
                info(f"d({a}) = {b}\td({b}) = {a}")
                result += a + b

    return result

if __name__ == "__main__":
    print(solve(10_000))
