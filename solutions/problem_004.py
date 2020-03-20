from common.math import is_palindrome

largest_palindrome = 0

for a in range(100, 1000):
    for b in range(a, 1000):
        product = a * b
        if product > largest_palindrome and is_palindrome(product):
            largest_palindrome = product

print(largest_palindrome)
