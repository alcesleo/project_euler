from common.primes import is_prime


TARGET = 0.1

n = 1
step = 2
total_diagonals = 1
diagonal_primes = set()

while True:
    for i in range(4):
        n += step
        total_diagonals += 1

        if is_prime(n):
            diagonal_primes.add(n)

    step += 2

    width = step - 1
    prime_ratio = len(diagonal_primes) / total_diagonals

    if prime_ratio < 0.1:
        print(width)
        break
