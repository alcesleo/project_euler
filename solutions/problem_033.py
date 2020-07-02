from fractions import Fraction
from common.logging import info

def solve():
    result = 1

    for n1 in range(1, 10):
        for d1 in range(n1 + 1, 10):
            for i in range(1, 10):

                n2 = n1 * 10 + i
                d2 = i * 10 + d1

                f1 = Fraction(n1, d1)
                f2 = Fraction(n2, d2)

                if f1 == f2:
                    info(f"{n2}/{d2} = {n1}/{d1}")
                    result *= f1

    return result.denominator


if __name__ == "__main__":
    print(solve())
