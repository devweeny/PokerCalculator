import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def isRed(self):
        return self.suit == "Hearts" or self.suit == "Diamonds"

    def __str__(self) -> str:
        return f"{self.number} of {self.suit}"


class Deck:
    """A class to represent a deck of cards."""

    def __init__(self):
        """Initialize the deck with 52 cards."""
        self.cards = []
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self._populate_deck()

    def _populate_deck(self):
        """Populate the deck with 52 cards."""
        for suit in self.suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))

    def shuffle(self):
        """Shuffle the deck of cards."""
        size = len(self.cards)
        for x in range(size):
            i = random.randint(0, size - 1)
            self.cards[x], self.cards[i] = self.cards[i], self.cards[x]

    def reshuffle(self):
        """Clear the deck and repopulate it."""
        self.cards.clear()
        self._populate_deck()

    def draw(self, amount):
        """Draw a specified amount of cards from the deck.
        Args:
            amount (int): The number of cards to draw.
        Returns:
            list: A list of drawn cards.
        """
        if amount > len(self.cards):
            raise IndexError("Not enough cards in the deck to draw.")
        return [self.cards.pop(0) for _ in range(amount)]

    def count(self):
        """Count the number of cards in the deck."""
        return len(self.cards)

    def __str__(self):
        """Return a string representation of the deck."""
        return str([str(c) for c in self.cards])

    def to_json(self):
        """Return a JSON representation of the deck."""
        return {
            "cards": self.cards
        }


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print(deck)
