from common.tools import split_digits

DIGITS = set(range(1, 10))


def unique_digits(n):
    """Returns the unique digits of n as a set, or None if any digits are repeated
    """
    d = split_digits(n)
    s = set(d)

    if len(d) == len(s):
        return s


limit = 2000
products = set()

for a in range(1, limit):
    digits_a = unique_digits(a)
    if not digits_a:
        continue

    for b in range(a + 1, limit):
        digits_b = unique_digits(b)
        if not digits_b:
            continue

        # a and b contain same digit
        if not digits_a.isdisjoint(digits_b):
            continue

        p = a * b

        digits_p = unique_digits(p)
        if not digits_p:
            continue

        no_common_digits = digits_a.isdisjoint(digits_b) and digits_b.isdisjoint(
            digits_p) and digits_p.isdisjoint(digits_a)

        contains_all_digits = (digits_a | digits_b | digits_p) == DIGITS

        if no_common_digits and contains_all_digits:
            products.add(p)


print(sum(products))
