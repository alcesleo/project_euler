from common.math import is_palindrome
from common.logging import info


def solve(limit):
    result = 0
    for n in range(1, limit):
        binary = f"{n:b}"

        if is_palindrome(n) and is_palindrome(binary):
            info(f"{n} = {binary}")
            result += n

    return result


if __name__ == "__main__":
    print(solve(1_000_000))
