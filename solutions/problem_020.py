import math
from common.tools import split_digits

TARGET = 100
print(sum(split_digits(math.factorial(TARGET))))
