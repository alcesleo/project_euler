def gen_collatz(start):
    n = start

    yield(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

        yield(n)


def solve(limit=1_000_000):
    longest_chain, starting_number = 0, 0

    for i in range(1, limit):
        sequence_length = len(list(gen_collatz(i)))

        if sequence_length > longest_chain:
            longest_chain, starting_number = sequence_length, i

    return starting_number


if __name__ == "__main__":
    print(solve())
