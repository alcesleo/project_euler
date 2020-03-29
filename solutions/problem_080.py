"""
The problem statement here is quite unclear about that you should include ALL digits of the
square root, not just the decimals. You have to be careful with the decimal precision and
rounding too, but not including the digits before the period lead me to submit the
wrong answer several times on this one.
"""

import decimal
from common.digits import split_digits

# Calculate more precision than needed to be sure to avoid rounding errors
context = decimal.Context(prec=105)
decimal.setcontext(context)


def solve(limit, digits):
    result = 0

    for n in range(limit + 1):
        root = decimal.Decimal(n).sqrt()

        if not float(root).is_integer():
            result += sum(split_digits(root)[:digits])

    return result


if __name__ == "__main__":
    print(solve(100, 100))
