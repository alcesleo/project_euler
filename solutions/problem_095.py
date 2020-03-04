from common.tools import proper_divisors

LIMIT = 1_000_000


def sum_proper_divisors_factory(limit):
    """Returns a function that returns the sum of proper divisors of numbers up to a limit, precalculated.
    Takes a while to generate but is then fast
    """
    sums = [0] * limit

    for i in range(1, limit):
        for m in range(i * 2, limit, i):
            sums[m] += i

    return sums.__getitem__


def sum_proper_divisors(n):
    """A sum_proper_divisors function without startup costs for quick tests
    """
    return sum(proper_divisors(n))


def amicable_chain(current, visited=[], next_fn=sum_proper_divisors):
    """Returns the numbers in an amicable chain in a list

    >>> amicable_chain(12496) # Amicable chain of 5 elements
    [12496, 14288, 15472, 14536, 14264]

    >>> amicable_chain(400) # Goes towards 0
    []

    >>> amicable_chain(276) # Goes towards infinity
    []

    >>> amicable_chain(284) # Amicable pair
    [220, 284]

    >>> amicable_chain(2362) # Terminates in an amicable pair
    [1210, 1184]

    >>> amicable_chain(28) # Perfect number
    [28]

    >>> amicable_chain(1235) # Terminates in perfect number
    [6]

    >>> amicable_chain(9464) # Terminates in chain
    []
    """
    # Found beginning of loop
    if len(visited) != 0 and visited[0] == current:
        return visited

    # Outside of bounds or terminates in chain
    if current <= 0 or current >= LIMIT or current in visited:
        return []

    next_number = next_fn(current)

    # Amicable pair
    if len(visited) != 0 and next_number == visited[-1]:
        return [current, visited[-1]]

    # Perfect number
    if next_number == current:
        return [current]

    return amicable_chain(next_number, visited + [current], next_fn=next_fn)


def solve():
    longest = 0
    smallest = 0
    next_fn = sum_proper_divisors_factory(LIMIT)

    for i in range(1, LIMIT):
        chain = amicable_chain(i, next_fn=next_fn)

        if len(chain) > longest:
            longest = len(chain)
            smallest = min(chain)

    return smallest


print(solve())
