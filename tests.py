import unittest
from deck import Deck, Card
from solitaire import Solitaire


class TestCard(unittest.TestCase):
    def setUp(self):
        """Create a new Card for each test."""
        self.card = Card(1, "Spades")

    def test_initial_card_number(self):
        """Test that a new card has the correct number."""
        self.assertEqual(self.card.number, 1)

    def test_initial_card_suit(self):
        """Test that a new card has the correct suit."""
        self.assertEqual(self.card.suit, "Spades")

    def test_initial_card_flipped(self):
        """Test that a new card is not flipped."""
        self.assertFalse(self.card.flipped)

    def test_flip(self):
        """Test that flipping the card changes its flipped status."""
        self.card.flip()
        self.assertTrue(self.card.flipped)

    def test_is_red(self):
        """Test that isRed method returns correct color."""
        self.assertFalse(self.card.isRed())
        self.card = Card(1, "Hearts")
        self.assertTrue(self.card.isRed())

    def test_get_symbol(self):
        """Test that get_symbol method returns correct symbol."""
        self.assertEqual(self.card.get_symbol(), "♠")
        self.card = Card(1, "Hearts")
        self.assertEqual(self.card.get_symbol(), "♥")

    def test_get_rank(self):
        """Test that get_rank method returns correct rank."""
        self.assertEqual(self.card.get_rank(), "A")
        self.card = Card(2, "Hearts")
        self.assertEqual(self.card.get_rank(), "2")

    def test_get_color_code(self):
        """Test that get_color_code method returns correct color code."""
        self.assertEqual(self.card.get_color_code(), "\033[37m")
        self.card = Card(1, "Hearts")
        self.assertEqual(self.card.get_color_code(), "\033[91m")

    def test_reset_color(self):
        """Test that reset_color method returns correct reset code."""
        self.assertEqual(self.card.reset_color(), "\033[0m")


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


class TestSolitaire(unittest.TestCase):
    def setUp(self):
        self.game = Solitaire()

    """Test that the deck from the library is empty"""

    def test_initial_deck(self):
        self.assertEqual(len(self.game.deck.cards), 0)

    """Test the difficulty is 1 by default"""

    def test_initial_difficulty(self):
        self.assertEqual(self.game.difficulty, 1)

    """Test that setting the difficulty is successful"""

    def test_set_difficulty(self):
        self.game.setDifficulty(2)
        self.assertEqual(self.game.difficulty, 2)
    """Test that the stock, and tableaus initally have the right length"""

    def test_deal(self):
        self.assertEqual(len(self.game.stock), 24)
        for i in range(7):
            self.assertEqual(len(self.game.tableau[i]), i+1)

    """Test that drawing on easy mode draws one card, and drawing on hard mode draws 3"""

    def test_draw(self):
        initial_stock_length = len(self.game.stock)
        self.game.draw()
        self.assertEqual(len(self.game.stock), initial_stock_length - 1)

        self.game.setDifficulty(2)
        initial_stock_length = len(self.game.stock)
        self.game.draw()
        self.assertEqual(len(self.game.stock), initial_stock_length - 3)


if __name__ == "__main__":
    unittest.main()
