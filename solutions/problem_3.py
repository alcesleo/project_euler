import math
from common import primes

LIMIT = 600851475143
biggest_factor = 0

for x in primes.gen_primes():
    if LIMIT % x == 0:
        biggest_factor = x

    if x > math.sqrt(LIMIT):
        break

print(biggest_factor)
