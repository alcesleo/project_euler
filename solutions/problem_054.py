from functools import total_ordering
from collections import Counter
from common.data import read_data


def read_poker_hands():
    poker_hands = []

    for cards in read_data("p054_poker.txt").splitlines():
        poker_hands.append((PokerHand(cards[:14]), PokerHand(cards[15:])))

    return poker_hands


@total_ordering
class Card:
    """
    >>> Card("5H") > Card("6C")
    False

    >>> Card("5H") == Card("5C")
    True
    """
    CARD_VALUES = {rank: value for value, rank in enumerate(
        ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"])}

    def __init__(self, card):
        self.rank, self.suit = card

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __lt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __hash__(self):
        return hash(self.value())

    def value(self):
        return self.CARD_VALUES[self.rank]


@total_ordering
class Rank:
    """
    >>> Rank("HIGH_CARD", Card("5H"))
    HIGH_CARD (5H)

    >>> Rank("HIGH_CARD", Card("5H")) == Rank("HIGH_CARD", Card("5C"))
    True

    >>> Rank("HIGH_CARD", Card("5H")) > Rank("PAIR", Card("3C"))
    False
    """
    RANK_VALUES = {rank: value for value, rank in enumerate([
        "HIGH_CARD", "PAIR", "TWO_PAIR", "THREE", "STRAIGHT", "FLUSH", "FULL_HOUSE", "STRAIGHT_FLUSH", "ROYAL_FLUSH"])}

    def __init__(self, rank, high_card):
        self.rank = rank
        self.high_card = high_card

    def __eq__(self, other):
        return self.rank == other.rank and self.high_card == other.high_card

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.value() < other.value()

        return self.high_card < other.high_card

    def __repr__(self):
        return f"{self.rank} ({self.high_card})"

    def value(self):
        return self.RANK_VALUES[self.rank]


class PokerHand:
    """
    >>> PokerHand("5H 5C 6S 7S KD").high_card()
    KD


    # Ranking hands
    >>> PokerHand("5D 8C 9S JS AC").rank()
    HIGH_CARD (AC)

    >>> PokerHand("5H 5C 6S 7S KD").rank()
    PAIR (5H)

    >>> PokerHand("5H 5C 6S 7S 7D").rank()
    TWO_PAIR (7S)

    >>> PokerHand("2D 9C AS AH AC").rank()
    THREE (AS)

    >>> PokerHand("3C 4D 5S 6S 7D").rank()
    STRAIGHT (7D)

    >>> PokerHand("3D 6D 7D TD QD").rank()
    FLUSH (QD)

    >>> PokerHand("3C 3D 3S 9S 9D").rank()
    FULL_HOUSE (3C)

    >>> PokerHand("3C 4C 5C 6C 7C").rank()
    STRAIGHT_FLUSH (7C)

    >>> PokerHand("TH JH QH KH AH").rank()
    ROYAL_FLUSH (AH)


    >>> PokerHand("5H 5C 6S 7S KD") > (PokerHand("2C 3S 8S 8D TD")) # PAIR 5 / PAIR 8
    False

    >>> PokerHand("5D 8C 9S JS AC") > (PokerHand("2C 5C 7D 8S QH")) # HIGH_CARD A / HIGH_CARD Q
    True

    >>> PokerHand("2D 9C AS AH AC") > (PokerHand("3D 6D 7D TD QD")) # THREE A / FLUSH Q
    False

    >>> PokerHand("4D 6S 9H QH QC") > (PokerHand("3D 6D 7H QD QS")) # PAIR Q (HIGH_CARD A) / PAIR Q (HIGH_CARD 7)
    True

    >>> PokerHand("2H 2D 4C 4D 4S") > (PokerHand("3C 3D 3S 9S 9D")) # FULL_HOUSE 4 / FULL_HOUSE 3
    True
    """

    def __init__(self, cards):
        self.cards = sorted([Card(c) for c in cards.split(" ")], reverse=True)

    def high_card(self):
        return self.cards[0]

    def is_flush(self):
        suits = [c.suit for c in self.cards]
        return len(set(suits)) == 1

    def is_straight(self):
        values = [c.value() for c in self.cards]
        return sorted(values) == list(range(min(values), max(values) + 1))

    def is_royal(self):
        ranks = [c.rank for c in self.cards]
        return set(ranks) == {"T", "J", "Q", "K", "A"}

    def rank(self):
        same_value = Counter(self.cards).most_common()
        card, card_count = same_value[0]
        second_card, second_card_count = same_value[1]

        if self.is_straight() and self.is_flush() and self.is_royal():
            return Rank("ROYAL_FLUSH", self.high_card())

        if self.is_straight() and self.is_flush():
            return Rank("STRAIGHT_FLUSH", self.high_card())

        if card_count == 4:
            return Rank("FOUR", card)

        if card_count == 3 and second_card_count == 2:
            return Rank("FULL_HOUSE", card)

        if self.is_flush():
            return Rank("FLUSH", self.high_card())

        if self.is_straight():
            return Rank("STRAIGHT", self.high_card())

        if card_count == 3:
            return Rank("THREE", card)

        if card_count == 2 and second_card_count == 2:
            return Rank("TWO_PAIR", max(card, second_card))

        if card_count == 2:
            return Rank("PAIR", card)

        return Rank("HIGH_CARD", self.high_card())

    def __gt__(self, other):
        if self.rank() != other.rank():
            return self.rank() > other.rank()

        for c1, c2 in zip(self.cards, other.cards):
            if c1 != c2:
                return c1 > c2


def solve():
    player1_wins = 0
    for player1, player2 in read_poker_hands():
        if player1 > player2:
            player1_wins += 1

    return player1_wins


print(solve())
