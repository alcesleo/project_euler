"""
Uses a Monte Carlo simulation to generate likelihoods of landing on squares.
It seems to work mostly well, though even at 10 million dice rolls (which
take close to 45s to execute) the percentages, especially for the third
most common square, are close enough to not yield completely stable results.

It solves the problem as it gets _mostly_ gets it right and otherwise narrows
it down to a few guesses, but it's frustrating not to get a stable result
in under 1m. Look into Markov Chains to improve th solution.
"""

from random import randint, sample
from collections import Counter
from common.logging import logger


SQUARES = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2",
]

COMMUNITY_CHEST = ["GO", "JAIL"] + [None] * 14

CHANCE = ["GO", "JAIL", "C1", "E3", "H2", "R1",
          "R+", "R+", "U+", "3-"] + [None] * 6


def roll(dice=2, faces=6):
    """Rolls the specified amount of dice with a certain number of faces and returns the sum. By default it rolls 2d6.
    """
    return [randint(1, faces) for _ in range(dice)]


def move(current_square, spaces):
    """Returns the next square that you would end up on moving a certain number of steps from where you are
    """
    next_square = SQUARES[
        (SQUARES.index(current_square) + spaces) % len(SQUARES)
    ]

    # Go to JAIL
    if next_square == "G2J":
        return "JAIL"

    # Community Chest
    if next_square.startswith("CC"):
        card = sample(COMMUNITY_CHEST, 1)[0]

        if card:
            return card
        else:
            return next_square

    # Chance
    if next_square.startswith("CH"):
        card = sample(CHANCE, 1)[0]

        if not card:
            return next_square

        if card in SQUARES:
            return card

        if card == "3-":
            return SQUARES[SQUARES.index(next_square) - 3]

        if card == "R+":
            next_railway = go_to_next(next_square, "R")
            return next_railway

        if card == "U+":
            next_utility = go_to_next(next_square, "U")
            return next_utility

    return next_square


def go_to_next(square, label):
    """Resolves which the next Utility or Railway square is based on the current square
    """
    return next(
        (s for s in SQUARES[SQUARES.index(square):] if s.startswith(label)), label + "1")


def monopoly(turns, dice_faces):
    """Simulates walking around the monopoly board a given number of turns.
    Returns the squares landed on in order as a list
    """
    visited_squares = Counter()
    current_square = "GO"
    consecutive_doubles = 0

    for i in range(turns):
        visited_squares.update((current_square,))

        dice = roll(2, dice_faces)

        # Three consecutive doubles = Go To JAIL
        if dice[0] == dice[1] and consecutive_doubles == 2:
            current_square = "JAIL"
            consecutive_doubles = 0
            continue
        if dice[0] == dice[1]:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0

        current_square = move(current_square, sum(dice))

    return visited_squares


def solve(dice_faces=6, turns=10_000):
    visited = monopoly(turns, dice_faces)
    result = ""

    for square, amount in visited.most_common()[:3]:
        result += f"{SQUARES.index(square):02}"

        percentage = amount / turns * 100
        logger.info(f"{square:>4}: {percentage:2.4f}%")

    return result


if __name__ == "__main__":
    print(solve(4, 1_000_000))
