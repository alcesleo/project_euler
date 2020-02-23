import itertools


def gen_collatz(start):
    n = start

    yield(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

        yield(n)


LIMIT = 1_000_000

longest_chain = 0
starting_number = 0

for i in range(1, LIMIT):
    sequence_length = len(list(gen_collatz(i)))
    if sequence_length > longest_chain:
        longest_chain = sequence_length
        starting_number = i


print(starting_number)
