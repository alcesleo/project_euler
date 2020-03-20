from common.digits import split_digits


def sum_of_digits_raised(n, power):
    return sum([x ** power for x in split_digits(n)])


POWER = 5

result = 0
limit = 500_000  # Found by trial and error

for n in range(2, limit):
    if n == sum_of_digits_raised(n, POWER):
        result += n

print(result)
