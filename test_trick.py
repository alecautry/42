import unittest
from main import Trick
from pygame_Dominos.domino import *

class TestTrick(unittest.TestCase):
    def setUp(self):
        self.trick = Trick()

    def test_trick_winner(self):
        # Test case where the first domino is the winning trump double
        dominos = [
            Domino(1, 6, 6, isTrump=True, isDouble=True),
            Domino(2, 5, 5, isTrump=True, isDouble=True),
            Domino(3, 4, 4, isTrump=True, isDouble=True),
            Domino(4, 3, 3, isTrump=True, isDouble=True)
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 1)

        # Test case where the second domino is the winning trump double
        dominos = [
            Domino(1, 6, 6, isTrump=True, isDouble=False),
            Domino(2, 5, 5, isTrump=True, isDouble=True),
            Domino(3, 4, 4, isTrump=True, isDouble=True),
            Domino(4, 3, 3, isTrump=True, isDouble=True)
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 2)

        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()