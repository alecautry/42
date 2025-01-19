# not* plain old data struct for Domino class
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
    # __lt__ and __gt__ are used to compare two Domino objects lt = < gt = >
    def __lt__(self, other):
        if not isinstance(other, Domino):
            return NotImplemented
        # self is always most important, so its the "lead domino"
        outcome = False # default true, because non matching suits
        # first determine if only one is trump
        if(self.isTrump != other.isTrump):
            if self.isTrump:
                outcome = False
            else:
                outcome = True
        elif(self.isTrump == other.isTrump):
            if(self.isDouble):
                return False
            elif(other.isDouble):
                return True
            elif(self.ID > other.ID):
                outcome = False
            else:
                outcome = True
            
        # next determine if "other" matches suit with "self"
        elif(self.highSide == other.highSide or self.highSide == other.lowSide):
            if(self.isDouble):
                outcome = False
            elif(other.isDouble):
                outcome = True
            elif(self.ID > other.ID):
                outcome = False
            else:
                outcome = True
        return outcome

    def __gt__(self, other):
        if not isinstance(other, Domino):
            return NotImplemented
        # self is always most important, so its the "lead domino"
        
        outcome = True # default true, because non matching suits
        # first determine if only one is trump
        if(self.isTrump != other.isTrump):
            if self.isTrump:
                outcome = True
            else:
                outcome = False
        
        # next determine if "other" matches suit with "self"
        elif(self.highSide == other.highSide or self.highSide == other.lowSide):
            if(self.isDouble):
                outcome = True
            elif(other.isDouble):
                outcome = False
            elif(self.ID > other.ID):
                outcome = True
            else:
                outcome = False
    
        return outcome
    def is_count(self):
        return (self.highSide + self.lowSide) % 5 == 0
    
    def ID_lookup(self, high, low):
        for domino in dominoSet:
            if domino.highSide == high and domino.lowSide == low:
                return domino.ID

# create a set of double-6 dominos
class DominoFactory:
    @staticmethod
    def create() -> list[Domino]:
        domino_set = [None] * 28  # Initialize list with 28 None elements
        id = 27
        for i in range(6, -1, -1):
            for j in range(6, -1, -1):
                if i >= j:
                    hi = i
                    lo = j
                    is_double = i == j
                    domino_set[id] = Domino(id, hi, lo, is_double, False)
                    id -= 1
        return domino_set

# Test and print
if __name__ == "__main__":
    dominoSet = DominoFactory.create()
    for dom in dominoSet:
        print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)