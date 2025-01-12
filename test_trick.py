import unittest
from main import Trick
from pygame_Dominos.domino import *


# 27:[6/6], 26:[6/5], 25:[6/4], 24:[6/3], 23:[6/2], 22:[6/1], 21:[6/0]
# 20:[5/5], 19:[5/4], 18:[5/3], 17:[5/2], 16:[5/1], 15: 5/0]
# 14:[4/4], 13:[4/3], 12:[4/2], 11:[4/1], 10:[4/0]
# 9:[3/3],  8:[3/2],  7:[3/1],  6:[3/0]
# 5:[2/2],  4:[2/1],  3:[2/0]
# 2:[1/1],  1:[1/0]
# 0:[0/0]
class TestTrick(unittest.TestCase):
    def setUp(self):
        self.trick = Trick()
        self.dominoSet = DominoFactory.create()

    def test_trick_winner(self):
        # Test case where the first domino is the winning trump double
        dominos = [
            self.dominoSet[27], # [6/6]
            self.dominoSet[26], # [6/5]
            self.dominoSet[25], # [6/4]
            self.dominoSet[24]  # [6/3]
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 1)

        # Test case where the second domino is the winning trump double TODO this is failing!!
        dominos = [
            self.dominoSet[26], # [6/5]
            self.dominoSet[27], # [6/6]
            self.dominoSet[25], # [6/4]
            self.dominoSet[24]  # [6/3]
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 2)

        # Test case where the third domino is the winning trump double
        dominos = [
            self.dominoSet[26], # [6/5]
            self.dominoSet[25], # [6/4]
            self.dominoSet[27], # [6/6]
            self.dominoSet[24]  # [6/3]
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 3)

        # Test case where the fourth domino is the winning trump double
        dominos = [
            self.dominoSet[26], # [6/5]
            self.dominoSet[25], # [6/4]
            self.dominoSet[27], # [6/3]
            self.dominoSet[24]  # [6/6]
        ]
        self.assertEqual(self.trick.trickWinner(dominos), 4)


if __name__ == "__main__":
    unittest.main()