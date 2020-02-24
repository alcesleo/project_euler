TARGET = 1000


def sum_of_digits(number):
    return sum([int(x) for x in str(number)])


result = sum_of_digits(2 ** TARGET)

print(result)
