LIMIT = 100


def sum_of_squares(up_to):
    return sum([x*x for x in range(up_to + 1)])


def square_of_sums(up_to):
    return sum(range(up_to + 1)) ** 2


result = square_of_sums(LIMIT) - sum_of_squares(LIMIT)

print(result)
