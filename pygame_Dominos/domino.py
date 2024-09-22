# plain old data struct for Domino class
class Domino:
    ID: int
    highSide: int
    lowSide: int
    isDouble: bool
    isTrump: bool

    def __init__(self, id, high, low, double, trump = False):
        self.ID = id
        self.highSide = high
        self.lowSide = low
        self.isDouble = double
        self.isTrump = trump

# create a set of double-6 dominos
class DominoFactory:
    @staticmethod
    def create() -> list[Domino]:
        domino_set = []
        id = 0
        for i in range(0, 7):
            for j in range(i, 7):
                # set features of domino
                hi = max(i, j)
                lo = min(i, j)
                is_double = False
                if i == j:
                    is_double = True
            
                domino_set.append(Domino(id, hi, lo, is_double, False))
                id += 1

        return domino_set

# Test and print
if __name__ == "__main__":
    dominoSet = DominoFactory.create()
    for dom in dominoSet:
        print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)