CHAIN_LENGTHS = {}


def chain_length(n):
    if n == 1:
        return 1

    if n in CHAIN_LENGTHS:
        return CHAIN_LENGTHS[n]

    CHAIN_LENGTHS[n] = 1 + chain_length(next_collatz(n))

    return CHAIN_LENGTHS[n]


def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1


def solve(limit):
    longest_chain, starting_number = 0, 0

    for i in range(1, limit):
        length = chain_length(i)

        if length > longest_chain:
            longest_chain, starting_number = length, i

    return starting_number


if __name__ == "__main__":
    print(solve(1_000_000))
