"""
Python has no issue working with numbers of this size, the only clever bit is using the modulo
operator to extract the last 10 digits, as turning it into a string **does** take a long time.
"""


def solve():
    return (28433 * 2 ** 7830457 + 1) % 10 ** 10


if __name__ == "__main__":
    result = solve()
    print(result)
