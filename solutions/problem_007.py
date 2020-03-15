from common.primes import gen_primes
from common.tools import nth

TARGET = 10_001

nth_prime = nth(gen_primes(), TARGET)

print(nth_prime)
