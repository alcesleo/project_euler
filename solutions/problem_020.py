import math
from common.digits import split_digits

TARGET = 100
print(sum(split_digits(math.factorial(TARGET))))
