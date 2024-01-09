import unittest
from deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        """Create a new Deck for each test."""
        self.deck = Deck()

    def test_initial_deck_size(self):
        """Test that a new deck has 52 cards."""
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle(self):
        """Test that shuffling changes the order of the cards."""
        cards_before_shuffle = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, cards_before_shuffle)

    def test_reshuffle(self):
        """Test that reshuffling resets the deck to 52 cards."""
        self.deck.draw(5)
        self.deck.reshuffle()
        self.assertEqual(len(self.deck.cards), 52)

    def test_draw(self):
        """Test that drawing reduces the deck size and returns the correct number of cards."""
        cards = self.deck.draw(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(self.deck.cards), 52 - 5)

    def test_draw_too_many(self):
        """Test that drawing more cards than are in the deck raises an exception."""
        with self.assertRaises(IndexError):
            self.deck.draw(53)


if __name__ == "__main__":
    unittest.main()
