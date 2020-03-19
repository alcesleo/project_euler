"""
I already made a Roman Numerals converter in Ruby a while back:

https://github.com/alcesleo/roman_numerals/blob/master/roman_numerals.rb
"""

from common.data import read_data


FACTORS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def to_arabic(roman_numeral):
    """Parses a (not necessarily well formed) roman numeral to an int

    >>> to_arabic("XVI")
    16

    >>> to_arabic("VVIIIIII")
    16

    >>> to_arabic("XXXXVIIII")
    49
    """
    result = 0

    for factor, roman in FACTORS:
        while roman_numeral.startswith(roman):
            result += factor
            roman_numeral = roman_numeral[len(roman):]

    return result


def to_roman(n):
    """Converts a number to a well formed roman numeral

    >>> to_roman(16)
    'XVI'

    >>> to_roman(49)
    'XLIX'
    """
    result = ""

    for factor, roman in FACTORS:
        times, n = divmod(n, factor)
        result += roman * times

    return result


def solve():
    data = read_data("p089_roman.txt").splitlines()
    result = 0

    for roman in data:
        arabic = to_arabic(roman)
        minimal_roman = to_roman(arabic)
        saved_characters = len(roman) - len(minimal_roman)

        result += saved_characters

    return result


if __name__ == "__main__":
    print(solve())
