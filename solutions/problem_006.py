def sum_of_squares(up_to):
    return sum([x*x for x in range(up_to + 1)])


def square_of_sums(up_to):
    return sum(range(up_to + 1)) ** 2


def solve(limit):
    return square_of_sums(limit) - sum_of_squares(limit)


if __name__ == "__main__":
    print(solve(100))
