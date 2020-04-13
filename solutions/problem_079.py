"""This one takes some deliberation, but the solution in the end is quite straightforward,
creating a graph of all digits which follow another digit and then searching through it to
find the shortest path that matches all login attempts.

I would certainly not place this in the 5% difficulty along with the very 1st problem though...
"""

from common.data import read_data


def validate(passcode, login):
    """Returns whether login appears in order within passcode.

    >>> validate("531278", "317")
    True

    >>> validate("123456", "256")
    True

    >>> validate("123456", "254")
    False

    >>> validate("125465", "545")
    True

    >>> validate("125546", "545")
    False
    """
    index = 0
    try:
        for digit in login:
            index = passcode.index(digit, index)
    except ValueError:
        return False

    return True


def validate_all(passcode, keylog):
    """Returns whether all logins in a keylog match a passcode.

    >>> validate_all("531278", {"317", "528"})
    True
    """
    return all(map(lambda login: validate(passcode, login), keylog))


def crack_passcode(keylog):
    """Cracks the passcode by creating a graph of which digits follow a certain digit,
    then performs a depth first search until it finds a passcode that matches all entries
    in the keylog.
    """
    follows = {str(i): set() for i in range(10)}

    for login in keylog:
        first, *rest = login
        follows[first] |= set(rest)

        second, *last = rest
        follows[second] |= set(last)

    for first in follows:
        passcode = depth_first_search(follows, first, keylog)

        if passcode:
            return passcode


def depth_first_search(follows, passcode, keylog):
    if validate_all(passcode, keylog):
        return passcode

    for neighbor in follows[passcode[-1]]:
        result = depth_first_search(follows, passcode + neighbor, keylog)
        if result:
            return result


def solve():
    keylog = read_data("p079_keylog.txt").splitlines()
    keylog = set(keylog)

    return crack_passcode(keylog)


if __name__ == "__main__":
    print(solve())
