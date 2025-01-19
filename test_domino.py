import unittest
from pygame_Dominos.domino import Domino, DominoFactory

def update_trump(domino_set, trump):
    for dom in domino_set:
        if dom.highSide == trump or dom.lowSide == trump:
            dom.isTrump = True
        else:
            dom.isTrump = False

# 27:[6/6], 26:[6/5], 25:[6/4], 24:[6/3], 23:[6/2], 22:[6/1], 21:[6/0]
# 20:[5/5], 19:[5/4], 18:[5/3], 17:[5/2], 16:[5/1], 15: 5/0]
# 14:[4/4], 13:[4/3], 12:[4/2], 11:[4/1], 10:[4/0]
# 9:[3/3],  8:[3/2],  7:[3/1],  6:[3/0]
# 5:[2/2],  4:[2/1],  3:[2/0]
# 2:[1/1],  1:[1/0]
# 0:[0/0]

class TestDomino(unittest.TestCase):
    def setUp(self):
        self.dominoSet = DominoFactory.create()
        update_trump(self.dominoSet, 7) # trump is empty
        self.doubles_ID = [0, 2, 5, 9, 14, 20, 27]
        self.ones_ID = [1, 2, 4, 7, 11, 16, 22]
        self.twos_ID = [3, 4, 5, 8, 12, 17, 23]
        self.threes_ID = [6, 7, 8, 9, 13, 18, 24]
        self.fours_ID = [10, 11, 12, 13, 14, 19, 25]
        self.fives_ID = [15, 16, 17, 18, 19, 20, 26]
        self.sixes_ID = [21, 22, 23, 24, 25, 26, 27]
        

    def test_less_than(self):
        # Test case where the first domino is less than the second domino
        domino1 = self.dominoSet[27]  # [6/6]
        domino2 = self.dominoSet[26]  # [6/5]
        self.assertFalse(domino1 < domino2)  # [6/6] is not less than [6/5]

        # Test case where the first domino is a double but the second domino is slightly bigger
        domino1 = self.dominoSet[0]  # [0/0]
        domino2 = self.dominoSet[1]  # [1/0]
        self.assertFalse(domino1 < domino2)  # [0/0] is not less than [1/0]

        # Test case where the dominos are not the same suit. 
        domino1 = self.dominoSet[27]  # [6/6]
        domino2 = self.dominoSet[14]  # [4/2]
        self.assertFalse(domino1 < domino2)  # [6/6] is not less than [4/2]

        # test case where the first domino is a trump and the second is a double
        update_trump(self.dominoSet, 2)
        domino1 = self.dominoSet[17]  # [5/2] this is a 2 trump, not a 5
        domino2 = self.dominoSet[20] # [5/5] This is not  a trump
        self.assertFalse(domino1 < domino2)
        update_trump(self.dominoSet, 7)

        update_trump(self.dominoSet, 0)
        # Test case where the first domino is a double but the second domino is slightly bigger
        domino1 = self.dominoSet[0]  # [0/0]
        domino2 = self.dominoSet[1]  # [1/0]
        self.assertTrue(domino2 < domino1)  # [1/0] is less than [0/0]
        update_trump(self.dominoSet, 7)
        # Add more test cases as needed
    def test_greater_than(self):
        # Test case where the first domino is less than the second domino
        domino1 = self.dominoSet[27]  # [6/6]
        domino2 = self.dominoSet[26]  # [6/5]
        self.assertTrue(domino1 > domino2)  # [6/6] is not less than [6/5]

        # Test case where the first domino is a double but the second domino is slightly bigger
        domino1 = self.dominoSet[0]  # [0/0]
        domino2 = self.dominoSet[1]  # [1/0]
        self.assertTrue(domino1 > domino2)  # [0/0] is not less than [1/0]

        # Test case where the dominos are not the same suit. 
        domino1 = self.dominoSet[27]  # [6/6]
        domino2 = self.dominoSet[14]  # [4/2]
        self.assertTrue(domino1 > domino2)  # [6/6] is not less than [4/2]

        # test case where the first domino is a trump and the second is a double
        update_trump(self.dominoSet, 2)
        domino1 = self.dominoSet[17]  # [5/2] this is a 2 trump, not a 5
        domino2 = self.dominoSet[20] # [5/5] This is not  a trump
        self.assertTrue(domino1 > domino2)
        update_trump(self.dominoSet, 7)

        #
        domino1 = self.dominoSet[26]  # [5/2] this is a 2 trump, not a 5
        domino2 = self.dominoSet[25] # [5/5] This is not  a trump
        self.assertTrue(domino1 > domino2)

        domino1 = self.dominoSet[26]  # [5/2] this is a 2 trump, not a 5
        domino2 = self.dominoSet[27] # [5/5] This is not  a trump
        self.assertFalse(domino1 > domino2)

        domino1 = self.dominoSet[27]  # [5/2] this is a 2 trump, not a 5
        domino2 = self.dominoSet[24] # [5/5] This is not  a trump
        self.assertTrue(domino1 > domino2)
    
    def test_all_doubles_gthan(self):
        
        for x in range(0,7):
            for domino in self.dominoSet:
                domino1 = self.dominoSet[self.doubles_ID[x]]
                domino2 = domino
                if(domino1 == domino2):
                    continue
                else:
                    self.assertTrue(domino1 > domino2)
    
    def test_0_1(self):
        domino1 = self.dominoSet[1]  # [1/0]'
        for x in range(0,7):
            print("x", x)
            update_trump(self.dominoSet, x)
            for domino in self.dominoSet:
                domino2 = domino
                if(domino1 == domino2):
                    continue
                elif(domino1.isTrump == True):
                    if(domino2.isTrump == True):
                        # write code to print out the dominos that are here with [high/low][id] format
                        print("domino1")
                        print(f"[{domino1.highSide}/{domino1.lowSide}][{domino1.ID}]")
                        print("domino2")
                        print(f"[{domino2.highSide}/{domino2.lowSide}][{domino2.ID}]")
                        
                        self.assertTrue(domino1 < domino2)
                    else:
                        self.assertTrue(domino1 > domino2)
                elif(domino2.isTrump == True):
                    self.assertTrue(domino1 < domino2)
                elif domino2.ID in self.ones_ID:
                    self.assertTrue(domino1 < domino2)
                else:
                    self.assertFalse(domino1 < domino2)
                    self.assertTrue(domino1 > domino2)
            update_trump(self.dominoSet, 7)
        update_trump(self.dominoSet, 7)
                    

if __name__ == "__main__":
    unittest.main()