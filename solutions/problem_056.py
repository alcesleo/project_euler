from common.digits import sum_digits

LIMIT = 100
maximum_sum = 0

for a in range(LIMIT):
    for b in range(LIMIT):
        digit_sum = sum_digits(a ** b)

        if digit_sum > maximum_sum:
            maximum_sum = digit_sum

print(maximum_sum)
