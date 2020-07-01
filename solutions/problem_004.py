from common.math import is_palindrome

def solve():
    largest_palindrome = 0

    for a in range(100, 1000):
        for b in range(a, 1000):
            product = a * b
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

if __name__ == "__main__":
    print(solve())
