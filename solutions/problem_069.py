from common.math import phi


def solve(limit=10):
    maximum_quotient = 0
    result = 0

    for n in range(1, limit + 1):
        totient = phi(n)
        quotient = n / totient

        if quotient > maximum_quotient:
            maximum_quotient = quotient
            result = n

    return result


if __name__ == "__main__":
    result = solve(1_000_000)
    print(result)
