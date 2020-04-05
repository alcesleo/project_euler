"""
We will always need 4 numbers and 3 operators in between them.

Only a single case of parenthesis actually matters: (ab)(cd), since
every other case of parenthesis can be rewritten to not use the parenthesis
with the numbers in a different order, thus is already covered by the permutations.
"""

from operator import add, sub, mul, truediv
from itertools import product, permutations, count
from common.digits import join_digits
from common.logging import logger

OPERATIONS = list(product([add, sub, mul, truediv], repeat=3))


def calculate(numbers, operations):
    """Returns the result of calculating the given numbers and operations.

    Disregarding order of operations and simply calculating left to right,
    where numbers are denoted abcd and operations XYZ this is equivalent to:
    a X b Y c Z d


    >>> calculate([2, 3, 4, 1], [add, mul, sub])
    19

    >>> calculate([1, 2, 3, 4], [add, mul, mul])
    36
    """
    result, *rest = numbers

    for number, operation in zip(rest, operations):
        result = operation(result, number)

    return result


def calculate_parenthesis(numbers, operations):
    """Returns the result of calculating the given numbers 2 at a time and then
    using the last operators on both results.

    Where numbers are denoted abcd and operations XYZ this is equivalent to:
    (a X b) Y (c Z d)

    >>> calculate_parenthesis([2, 3, 4, 1], [add, truediv, add])
    1
    """
    a, b, c, d = numbers
    x, y, z = operations

    return int(y(x(a, b), z(c, d)))


def targets(numbers):
    """Returns all possible positive integer targets of the given numbers.

    >>> targets([1, 2, 3, 4])
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 36}

    >>> len(targets([1, 2, 3, 4]))
    31
    """
    result = set()

    for digits in permutations(numbers):
        for operations in OPERATIONS:
            target = calculate(digits, operations)

            logger.debug(f"{target} ({operations})")

            if target >= 1 and float(target).is_integer():
                result.add(int(target))

            target = calculate_parenthesis(digits, operations)

            if target >= 1 and float(target).is_integer():
                result.add(int(target))

    return result


def consecutive_positive_integers(numbers):
    """Returns the number of consecutive positive integers 1 to n in a given set.

    >>> consecutive_positive_integers(targets([1, 2, 3, 4]))
    28
    """

    for i in count(1):
        if i not in numbers:
            return i - 1


def solve():
    longest = (0, [])

    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    digits = [a, b, c, d]
                    length = consecutive_positive_integers(
                        targets(digits))

                    logger.info(f"{digits}: {length}")

                    if length > longest[0]:
                        longest = (length, digits)

    return join_digits(longest[1])


if __name__ == "__main__":
    print(solve())
