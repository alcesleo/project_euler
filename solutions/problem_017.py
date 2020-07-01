TWENTY = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS = [
    None,
    None,
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def number_to_english(n):
    if n < 20:
        return TWENTY[n]

    if n < 100:
        result = TENS[n // 10]

        if n % 10 != 0:
            result += "-" + number_to_english(n % 10)

        return result

    if n < 1000:
        result = number_to_english(n // 100) + " hundred"

        if n % 100 != 0:
            result += " and " + number_to_english(n % 100)

        return result

    if n < 1001:
        result = number_to_english(n // 1000) + " thousand"
        return result


def number_of_letters(text):
    return len(text.replace("-", "").replace(" ", ""))


def solve(limit):
    """
    >>> solve(5)
    19
    """
    return sum([number_of_letters(number_to_english(n))
               for n in range(1, limit + 1)])

if __name__ == "__main__":
    print(solve(1000))
