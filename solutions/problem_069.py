def phi(n):
    """Returns the Euler's Totient of n, i.e. the number of relative primes to n below n.

    https://www.geeksforgeeks.org/eulers-totient-function/
    """
    # Initialize result as n
    result = n
    p = 2

    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n //= p

            result -= result // p

        p += 1

    if (n > 1):
        result -= result // n

    return result


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
