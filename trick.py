class Trick:
    def __init__(self):
        self.trick = []
        self.playerIndex = []

    def trickWinner(self, theTrick): # TODO
        #  trickWinner2(d1: Domino, d2: Domino, d3: Domino, d4: Domino) -> int:
        # dlead = d1
        d1 = theTrick[0]
        d2 = theTrick[1]
        d3 = theTrick[2]
        d4 = theTrick[3]
        if(d1 > d2):
            if(d1 > d3):
                if(d1 > d4):
                    return 0
                else:
                    return 3
            elif(d3 > d4):
                return 2
            else:
                return 3
        elif(d2 > d3):
            if(d2 > d4):
                return 1
            else:
                return 3
        elif(d3 > d4):
            return 2
        else:
            return 3
    
    def printTrick(self):
        for domino in self.trick:
            i = 0
            print(f"[{domino.highSide}/{domino.lowSide}][{self.playerIndex[i]}]")
            i += 1
