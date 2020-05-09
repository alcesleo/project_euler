from functools import lru_cache


@lru_cache(maxsize=1_000_000)
def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1


@lru_cache(maxsize=1_000_000)
def chain_length(n):
    if n == 1:
        return 1

    return 1 + chain_length(next_collatz(n))


def solve(limit=1_000_000):
    longest_chain, starting_number = 0, 0

    for i in range(1, limit):
        length = chain_length(i)

        if length > longest_chain:
            longest_chain, starting_number = length, i

    return starting_number


if __name__ == "__main__":
    print(solve())
