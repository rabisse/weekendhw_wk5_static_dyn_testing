import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("H", 8)
        self.card2 = Card("D", 1)
        self.cardgame = CardGame(self.card1, self.card2)
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace())
    
    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card())

    def test_cards_total(self):
        self.assertEqual("You have a total of 9", self.cardgame.cards_total())
