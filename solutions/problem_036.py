from common.tools import is_palindrome


def binary(n):
    return f"{n:b}"


LIMIT = 1_000_000

result = 0
for n in range(1, LIMIT):
    if is_palindrome(n) and is_palindrome(binary(n)):
        result += n

print(result)
