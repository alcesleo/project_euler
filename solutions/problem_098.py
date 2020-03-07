from itertools import permutations
from collections import defaultdict
from common.data import read_strs
from common.tools import concatenate_digits


def find_anagrams(words):
    """Returns a list of anagram-pairs
    """
    anagrams = defaultdict(list)

    for word in words:
        letters = list(word)
        letters.sort()

        anagrams[tuple(letters)].append(word)

    return list(filter(lambda a: len(a) > 1, anagrams.values()))


def largest_anagramic_square(word, anagram, *ignore):
    """Returns the biggest square of a pair of anagrams if they are both square, otherwise 0

    If more than a pair is given, the following anagrams are ignored (there's only a single case and it's short)

    >>> largest_anagramic_square("CARE", "RACE")
    9216
    """

    mapping = {letter: index for (index, letter) in enumerate(set(word))}
    largest = 0

    for numbers in permutations(range(1, 10), len(mapping)):
        w = replace_letters(word, numbers, mapping)
        a = replace_letters(anagram, numbers, mapping)

        if is_square(w) and is_square(a) and max(w, a) > largest:
            largest = max(w, a)

    return largest


def replace_letters(word, numbers, mapping):
    """Constructs a number from a word, replacing the letters with numbers based on indexes in mapping

    >>> replace_letters("CARE", (1, 9, 6, 2), {'C': 0, 'R': 1, 'E': 2, 'A': 3})
    1296

    >>> replace_letters("RACE", (1, 9, 6, 2), {'C': 0, 'R': 1, 'E': 2, 'A': 3})
    9216
    """
    return concatenate_digits(numbers[mapping[letter]] for letter in word)


def is_square(n):
    return (n ** 0.5).is_integer()


def solve():
    words = read_strs("p098_words.txt")
    anagrams = find_anagrams(words)
    largest = 0

    for pair in anagrams:
        square = largest_anagramic_square(*pair)
        if square > largest:
            largest = square

    return largest


print(solve())
