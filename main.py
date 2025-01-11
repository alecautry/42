import random
from pygame_Dominos.domino import *



class GameState:
    # Shuffle and deal dominoes
    INIT = "INIT"

    # Players place bids to determine who goes first
    BID = "BID"

    # Play the game: players take turns placing dominoes
    PLAYING = "PLAYING"

    # Game is over: calculate scores and determine winner
    GAME_OVER = "GAME_OVER"

class HumanPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play(self, dominoSet):
        print("Your turn, ", self.name)
        print("Your dominoes:")
        for dom in dominoSet:
            print(f"[{dom.highSide}/{dom.lowSide}][{dom.ID}]")
        dominoID = input("Enter the ID of the domino you want to play: ")
        for dom in dominoSet:
            if dom.ID == int(dominoID):
                self.hand.remove(dom)
                return dom
        return None

    def filter_legal_moves(self, dominoSet, lead_domino):
        # Placeholder for logic to filter legal moves
        # Example: Only allow dominoes that match any of the lead domino's high or low sides
        if lead_domino:
            legal_moves = [dom for dom in dominoSet if any(dom.highSide == ld.highSide or dom.lowSide == ld.highSide for ld in lead_domino)]
            if legal_moves:
                return legal_moves
        return dominoSet
    
    def get_bid(self, current_bid):
        legalBid = False
        while (not legalBid):
            bid = int(input(f"{self.name}, enter your bid: "))
            if(current_bid > bid):
                
                print("Invalid bid, must be higher than the current bid.")
                print(f"Current bid is {current_bid}")
            else:
                legalBid = True
            
        return bid

class ComputerPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play(self, dominoSet):
        print("Computer's turn, ", self.name)
        print("Computer's dominoes:")
        for dom in dominoSet:
            print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)
        
        # Simple AI logic to select a domino to play
        selected_domino = self.select_domino(dominoSet)
        if selected_domino:
            self.hand.remove(selected_domino)
        return selected_domino

    def select_domino(self, dominoSet):
        # Placeholder for AI logic to select a domino
        # Example: Select the highest double if available
        for dom in dominoSet:
            if dom.isDouble:
                return dom
        # If no doubles, return the first domino
        return dominoSet[0] if dominoSet else None

    def filter_legal_moves(self, dominoSet, lead_domino):
        # Placeholder for logic to filter legal moves
        # Example: Only allow dominoes that match any of the lead domino's high or low sides
        if lead_domino:
            legal_moves = [dom for dom in dominoSet if any(dom.highSide == ld.highSide or dom.lowSide == ld.highSide for ld in lead_domino)]
            if legal_moves:
                return legal_moves
        return dominoSet

    def get_bid(self, current_bid):
        if(current_bid == 42):
            return 42
        
        bid = random.randint(current_bid+1, 42)  # Simple AI for bidding (30 is the min)
        return bid
    
    def set_trump(self):
        trump = random.randint(0,6)
        return trump

class Trick:
    def __init__(self):
        self.trick = []

    def trickWinner(self, theTrick): # TODO
        #  trickWinner2(d1: Domino, d2: Domino, d3: Domino, d4: Domino) -> int:
        # dlead = d1
        d1 = theTrick[0]
        d2 = theTrick[1]
        d3 = theTrick[2]
        d4 = theTrick[3]

        if(d1.isTrump & d1.isDouble):
            return 1
        elif(d2.isTrump & d2.isDouble):
            return 2
        elif(d3.isTrump & d3.isDouble):
            return 3
        elif(d4.isTrump & d4.isDouble):
            return 4

        #if all trump compare ID
        if(d1.isTrump and d2.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, d2.ID, d3.ID, d4.ID)
        #if d4 isn't trump
        elif(d1.isTrump and d2.isTrump and d3.isTrump):
            return self.compareThree(d1.ID, d2.ID, d3.ID)
        #if d3 isn't trump
        elif(d1.isTrump and d2.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, d2.ID, -1, d4.ID)
        #if d2 isn't trump
        elif(d1.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, -1, d3.ID, d4.ID)
        #if d1 isn't trump
        elif(d2.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(-1, d2.ID, d3.ID, d4.ID)
        #if d1 and d2
        elif(d1.isTrump and d2.isTrump):
            return self.compareTwo(d1.ID, d2.ID)
        #if d1 and d3
        elif(d1.isTrump and d3.isTrump):
            return self.compareThree(d1.ID , -1, d3.ID)
        #if d1 and d4
        elif(d1.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, -1,-1, d4.ID)
        #if d2 and d3
        elif(d2.isTrump and d3.isTrump):
            return self.compareFour(-1,d2.ID,d3.ID,-1)
        #if d2 and d4
        elif(d2.isTrump and d4.isTrump):
            return self.compareFour(-1,d2.ID,-1,d4.ID)
        #if d3 and d4
        elif(d3.isTrump and d4.isTrump):
            return self.compareFour(-1,-1,d3.ID,d4.ID)
        elif(d1.isTrump):
            return 1
        elif(d2.isTrump):
            return 2
        elif(d3.isTrump):
            return 3
        elif(d4.isTrump):
            return 4

        # At this point we have no Trump
        # d1 is always lead
        if(d1.isDouble):
            return 1
        # if d2 is a double and matches the high side of d2 lead it is the highest double 
        elif d2.isDouble and (d2.highSide == d1.highSide): 
            return 2
        elif d3.isDouble and (d3.highSide == d1.highSide):
            return 3
        elif d4.isDouble and (d4.highSide == d1.highSide):
            return 4

        # No doubles matching Lead suit
        # Compare highside and ID
        if((d2.highSide == d1.highSide) and (d3.highSide == d1.highSide) and (d4.highSide == d1.highSide)):
            return self.compareFour(d1.ID, d2.ID, d3.ID, d4.ID)
        #now compare 3
        # if 1, 2, and 3 have highside but not 4
        elif((d2.highSide == d1.highSide) and (d3.highSide == d1.highSide)):
            return self.compareFour(d1.ID, d2.ID, d3.ID, -1)
        # if 1, 2, and 4 have highside but not 3
        elif((d2.highSide == d1.highSide) and (d4.highSide == d1.highSide)):
            return self.compareFour(d1.ID, d2.ID, -1, d4.ID)
        # if 1 and 2 but not 3 and 4
        elif(d2.highSide == d1.highSide):
            return self.compareFour(d1.ID, d2.ID, -1, -1)
        # if 1 and 3 but not 2 and 4
        elif(d3.highSide == d1.highSide):
            return self.compareFour(d1.ID, -1, d3.ID, -1)
        # if 1 and 4 but not 2 and 3
        elif(d4.highSide == d1.highSide):
            return self.compareFour(d1.ID, -1, -1, d4.ID)

        # I think this is everything?
        # if nothing matches, return 1
        return 1

    #this will return 1 or 2. Which ever is highest
    def compareTwo(intOne: int, intTwo: int) -> int:
        if (intOne > intTwo):
            return 1
        else:
            return 2
        
            #this will return 1, 2, or 3. Which ever is the highest
    def compareFour(intOne: int, intTwo: int, intThree: int, intFour: int):
        if(intOne > intTwo):
            if(intOne > intThree):
                if(intOne > intFour):
                    return 1
                else:
                    return 4
            elif(intThree > intFour):
                return 3
            else:
                return 4
        elif(intTwo > intThree):
            if(intTwo > intFour):
                return 2
            else:
                return 4
        elif(intThree > intFour):
            return 3
        else:
            return 4

    def compareThree(intOne: int, intTwo: int, intThree: int) -> int:
        if( intOne > intTwo):
            if(intOne > intThree):
                return 1
            else:
                return 3
        elif (intTwo > intThree):
            return 2
        else:
            return 3

class Game:
    def __init__(self):
        self.state = GameState.INIT
        self.players = [HumanPlayer("Player 1"), ComputerPlayer("Player 2"), HumanPlayer("Player 3"), ComputerPlayer("Player 4")]
        self.trick = Trick()
        self.teamOneTricks = []
        self.teamTwoTricks = []
        self.dominoSet = []
        self.trump = None

    def run(self):
        while True:
            if self.state == GameState.INIT:
                self.initialize_game()
                self.state = GameState.BID

            elif self.state == GameState.BID:
                self.bidding_phase()
                self.state = GameState.PLAYING

            elif self.state == GameState.PLAYING:
                self.playing_phase()
                self.state = GameState.GAME_OVER

            elif self.state == GameState.GAME_OVER:
                self.game_over()
                break

        input("Press Enter to exit...")

    def initialize_game(self):
        print("Initializing game...")
        # Create each Domino
        self.dominoSet = DominoFactory.create()
        for dom in self.dominoSet:
            print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)

        # Determine who will go first
        self.current_player_index = random.randint(0, 3)
        print(f"Player {self.current_player_index + 1} will go first.")
    
        # Shuffle and deal dominoes
        self.deal_and_shuffle()
        for dom in self.dominoSet:
            print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)
        for player in self.players:
            print(player.name)
            for dom in player.hand:
                print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)


    def bidding_phase(self):
        print("Bidding phase...")
        bids = []
        bid = 0

        for player in self.players:

            bid = player.get_bid(bid)
            bids.append(bid)
            print(f"{player.name} bids {bid}")

        highest_bid = max(bids)
        winner_index = bids.index(highest_bid)
        print(f"{self.players[winner_index].name} wins the bid with {highest_bid}")

        # Winner sets the trump
        self.set_trump(winner_index)

        # Set the current player to the winner of the bid
        self.current_player_index = winner_index


    def playing_phase(self):
        print("Playing phase...")
        self.play_tricks()

    def game_over(self):
        print("Game over!")
        self.calculate_scores()

    def deal_and_shuffle(self):
        random.shuffle(self.dominoSet)

        for x in range(0, 7):
            self.players[0].hand.append(self.dominoSet[x])
            self.players[1].hand.append(self.dominoSet[x + 7])
            self.players[2].hand.append(self.dominoSet[x + 14])
            self.players[3].hand.append(self.dominoSet[x + 21])
        return True

    def set_trump(self, winner_index):
        # Ask the winner to set the trump
        if isinstance(self.players[winner_index], HumanPlayer):
            self.trump = int(input(f"{self.players[winner_index].name}, set the trump (0-6): "))
        else:
            self.trump = self.players[winner_index].set_trump()
        print(f"Trump is set to {self.trump}")

        for player in self.players:
            for each in player.hand:
                if each.highSide == self.trump or each.lowSide == self.trump:
                    each.isTrump = True

    def play_tricks(self):
        # Play tricks and determine the winner of each trick
        # the winner plays in order
        # after 4 dominos are played to the TRICK
        # a winner is determined and the next player plays
        # the game stops when all dominos have been played
        # the winner is determined if the bidding team makes their bid or not
        for x in range(0, 7):
            for _ in range(4):
                player = self.players[self.current_player_index]
                legal_moves = player.filter_legal_moves(player.hand, self.trick.trick[0] if self.trick.trick else None)
                domino = player.play(legal_moves)
                print(f"{player.name} plays domino [{domino.highSide}/{domino.lowSide}][{domino.ID}]")
                self.trick.trick.append(domino)
                self.current_player_index = (self.current_player_index + 1) % 4

            winner = self.trick.trickWinner(self.trick.trick)
            team = "Team 1" if winner % 2 == 0 else "Team 2"
            print(f"Player {winner} wins the trick for {team}!")
            self.current_player_index = winner
            self.trick.trick = []
            if winner == 0 or winner == 2:  # player 1 and 3, Team 1
                self.teamOneTricks.append(winner)
            else:  # player 2 and 4, Team 2
                self.teamTwoTricks.append(winner)


    def calculate_scores(self):
        # Calculate scores and determine the winner
        pass

if __name__ == "__main__":
    game = Game()
    game.run()