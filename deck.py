import random
import os


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.flipped = False

    def flip(self):
        self.flipped = True

    def isRed(self):
        return self.suit == "Hearts" or self.suit == "Diamonds"

    def get_symbol(self):
        symbols = {
            "Hearts": "♥",
            "Diamonds": "♦",
            "Clubs": "♣",
            "Spades": "♠"
        }
        return symbols.get(self.suit)

    def get_rank(self):
        ranks = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        return ranks.get(self.number, str(self.number))

    def get_color_code(self):
        return "\033[91m" if self.isRed() else '\033[37m'

    def reset_color(self):
        return "\033[0m"

    def __str__(self):
        symbol = self.get_symbol()
        color_code = self.get_color_code()
        reset_code = self.reset_color()
        rank = self.get_rank()
        return f"{color_code}{rank} {symbol}{reset_code}"


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self._populate_deck()
        if (os.name == 'nt'):
            os.system('color')

    def _populate_deck(self):
        for suit in self.suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))

    def shuffle(self):
        size = len(self.cards)
        for x in range(size):
            i = random.randint(0, size - 1)
            self.cards[x], self.cards[i] = self.cards[i], self.cards[x]

    def reshuffle(self):
        self.cards.clear()
        self._populate_deck()

    def draw(self, amount):
        if amount > len(self.cards):
            raise IndexError("Not enough cards in the deck to draw.")
        return [self.cards.pop(0) for _ in range(amount)]

    def count(self):
        return len(self.cards)

    def __str__(self):
        return str([str(c) for c in self.cards])

    def to_json(self):
        return {
            "cards": self.cards
        }


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print(deck)
