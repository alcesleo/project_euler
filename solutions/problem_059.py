from itertools import cycle, islice, product
from collections import Counter
from common.data import read_data, parse_list


def cipher(data, key):
    cycle_key = list(islice(cycle(map(ord, key)), len(data)))

    result = ""
    for char, k in zip(data, cycle_key):
        result += chr(char ^ k)

    return result


def heuristic(text):
    """Return a score of the text based on whether it has many common letters
    """
    c = Counter(text)
    score = 0
    positive = ["e", "t", "a", "o"]

    for letter in positive:
        score += c[letter]

    return score


def brute_force(data):
    """Try all passwords and return the deciphered result with the highest heuristic score
    """
    lower_case = list(map(chr, range(ord("a"), ord("z") + 1)))
    passwords = list(product(lower_case, repeat=3))

    high_score = 0
    result = None

    for password in passwords:
        text = cipher(data, password)
        score = heuristic(text)

        if score > high_score:
            high_score = score
            result = text

    return result


def solve():
    data = read_data("p059_cipher.txt")
    data = parse_list(data, separator=",", parse_item=int)

    text = brute_force(data)

    return sum((map(ord, text)))


print(solve())
