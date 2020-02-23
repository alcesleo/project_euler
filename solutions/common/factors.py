from functools import reduce

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python


def factors(n):
    """Returns all the factors of n as a set
    """
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
