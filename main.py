import random
from pygame_Dominos.domino import *
import unittest
import sys


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
        for index, dom in enumerate(dominoSet):
            print(f"{index}: [{dom.highSide}/{dom.lowSide}]")
        dominoIndex = input("Enter the index of the domino you want to play: ")
        try:
            dominoIndex = int(dominoIndex)
            if 0 <= dominoIndex < len(dominoSet):
                dom = dominoSet[dominoIndex]
                self.hand.remove(dom)
                return dom
            else:
                print("Invalid index. Please try again.")
                return self.play(dominoSet)  # Recursively call play to retry
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.play(dominoSet)  # Recursively call play to retry

    def filter_legal_moves(self, dominoSet, lead_domino):
        # Only allow dominoes that match the lead domino's high side or are trumps if the lead domino is a trump
        if lead_domino:
            if lead_domino.isTrump:
                legal_moves = [dom for dom in dominoSet if dom.isTrump]
            else:
                legal_moves = [dom for dom in dominoSet if dom.highSide == lead_domino.highSide or dom.lowSide == lead_domino.highSide]
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
        if(DEBUG):
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
        # Only allow dominoes that match the lead domino's high side or are trumps if the lead domino is a trump
        if lead_domino:
            if lead_domino.isTrump:
                legal_moves = [dom for dom in dominoSet if dom.isTrump]
            else:
                legal_moves = [dom for dom in dominoSet if dom.highSide == lead_domino.highSide or dom.lowSide == lead_domino.highSide]
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

class Game:
    def __init__(self):
        self.state = GameState.INIT
        self.players = [HumanPlayer("Player 1"), ComputerPlayer("Player 2"), ComputerPlayer("Player 3"), ComputerPlayer("Player 4")]
        self.trick = Trick()
        self.teamOneTricks = []
        self.teamTwoTricks = []
        self.dominoSet = []
        self.trump = None
        self.teamOneScore = 0
        self.teamTwoScore = 0
        

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

        # Determine who will go first
        self.current_player_index = random.randint(0, 3)
        print(f"Player {self.current_player_index + 1} will go first.")
    
        # Shuffle and deal dominoes
        self.deal_and_shuffle()
        #if debug, print each players hand
        if(DEBUG):
            print("Printing Each Players Hand")
            for player in self.players:
                print(player.name)
                for dom in player.hand:
                    print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)
        print("---------------------------------")


    def bidding_phase(self):
        print("Bidding phase...")
        bids = []
        bid = 0

        start_index = self.current_player_index  # Start from the current player index

        for i in range(len(self.players)):
            player_index = (start_index + i) % len(self.players)
            player = self.players[player_index]

            bid = player.get_bid(bid)
            bids.append(bid)
            print(f"{player.name} bids {bid}")

        highest_bid = max(bids)
        winner_index = (start_index + bids.index(highest_bid)) % len(self.players)
        print(f"{self.players[winner_index].name} wins the bid with {highest_bid}")

        # Winner sets the trump
        self.set_trump(winner_index)

        # Set the current player to the winner of the bid
        self.current_player_index = winner_index
        print("---------------------------------")


    def playing_phase(self):
        print("Playing phase...")
        self.play_tricks()
        print("---------------------------------")

    def game_over(self):
        print("Game over!")
        self.calculate_scores()
        print("---------------------------------")

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
            trick_order = []  # Temporary array to store the order of each domino played
            for _ in range(4):
                player = self.players[self.current_player_index]
                legal_moves = player.filter_legal_moves(player.hand, self.trick.trick[0] if self.trick.trick else None)
                domino = player.play(legal_moves)
                print(f"{player.name} plays domino [{domino.highSide}/{domino.lowSide}][{domino.ID}]")
                self.trick.trick.append(domino)
                self.trick.playerIndex.append(self.current_player_index)
                trick_order.append(self.current_player_index)  # Store the player index
                self.current_player_index = (self.current_player_index + 1) % 4
            
            # Print each domino in the trick along with the player index
            print("---------------------------------")
            for i, domino in enumerate(self.trick.trick):
                player_index = trick_order[i]
                print(f"[{domino.highSide}/{domino.lowSide}][{player_index}]")
            print("---------------------------------")
            winner_index_in_trick = self.trick.trickWinner(self.trick.trick)
            winner_player_index = trick_order[winner_index_in_trick]
            team = "Team 1" if winner_player_index % 2 == 0 else "Team 2"
            print(f"Player {winner_player_index + 1} wins the trick for {team}!")
            print("---------------------------------")
            # Update scores
            if team == "Team 1":
                self.teamOneScore += 1
            else:
                self.teamTwoScore += 1

            # Check for count dominos and update scores
            for domino in self.trick.trick:
                if domino.is_count():
                    if team == "Team 1":
                        self.teamOneScore += (domino.highSide + domino.lowSide)
                    else:
                        self.teamTwoScore += (domino.highSide + domino.lowSide)

            self.current_player_index = winner_player_index  # Set the next starting player to the winner
            self.trick.trick = []
            if winner_player_index == 0 or winner_player_index == 2:  # player 1 and 3, Team 1
                self.teamOneTricks.append(winner_player_index)
            else:  # player 2 and 4, Team 2
                self.teamTwoTricks.append(winner_player_index)

        print(f"Final Scores - Team 1: {self.teamOneScore}, Team 2: {self.teamTwoScore}")
    



    def calculate_scores(self):
        # Calculate scores and determine the winner
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import test_trick  # Import the test module
        unittest.main(module='test_trick', argv=[sys.argv[0]])  # Run unit tests
    else:
        DEBUG = False
        game = Game()
        game.run()