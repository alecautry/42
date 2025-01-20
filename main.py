import random
from pygame_Dominos.domino import *
import unittest
import sys
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("42 Domino Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Define standard coordinates for drawing dominos in the middle of the screen
MIDDLE_X = 250
MIDDLE_Y = 200
DOMINO_WIDTH = 50
DOMINO_HEIGHT = 50
DOMINO_SPACING = 60

class GameState:
    # Shuffle and deal dominoes
    INIT = "INIT"

    # Players place bids to determine who goes first
    BID = "BID"

    # Play the game: players take turns placing dominoes
    PLAYING = "PLAYING"

    # Game is over: calculate scores and determine winner
    GAME_OVER = "GAME_OVER"

    QUIT = "QUIT"

class HumanPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play(self, dominoSet, playedDominos=None):
        if not TEXT_INPUT:
            selected_domino = self.display_play_popup(dominoSet, playedDominos)
        else:
            print("Your turn, ", self.name)
            print("Your dominoes:")
            for index, dom in enumerate(dominoSet):
                print(f"{index}: [{dom.highSide}/{dom.lowSide}]")
            dominoIndex = input("Enter the index of the domino you want to play: ")
            try:
                dominoIndex = int(dominoIndex)
                if 0 <= dominoIndex < len(dominoSet):
                    selected_domino = dominoSet[dominoIndex]
                else:
                    print("Invalid index. Please try again.")
                    return self.play(dominoSet)  # Recursively call play to retry
            except ValueError:
                print("Invalid input. Please enter a number.")
                return self.play(dominoSet)  # Recursively call play to retry

        self.hand.remove(selected_domino)
        return selected_domino

    def display_play_popup(self, dominoSet, playedDominos):
        selected_domino = None
        running = True
        font = pygame.font.Font(None, 36)
        button_rects = []

        # Determine legal moves
        lead_domino = playedDominos[0] if playedDominos else None
        legal_moves = self.filter_legal_moves(self.hand, lead_domino)

        # Create buttons for legal dominos in hand
        for i, dom in enumerate(self.hand):
            if dom in legal_moves:
                button_rects.append((pygame.Rect(MIDDLE_X + i * DOMINO_SPACING, 400, DOMINO_WIDTH, DOMINO_HEIGHT), dom))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, dom in button_rects:
                        if rect.collidepoint(event.pos):
                            selected_domino = dom
                            running = False

            # Clear the middle area
            pygame.draw.rect(screen, WHITE, pygame.Rect(MIDDLE_X, MIDDLE_Y, 300, 200))

            # Draw played dominos
            for i, dom in enumerate(playedDominos):
                text = font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
                screen.blit(text, (MIDDLE_X + i * DOMINO_SPACING, MIDDLE_Y))

            # Draw all dominos in hand
            for i, dom in enumerate(self.hand):
                rect = pygame.Rect(MIDDLE_X + i * DOMINO_SPACING, 400, DOMINO_WIDTH, DOMINO_HEIGHT)
                if rect.collidepoint(pygame.mouse.get_pos()):
                    color = RED if dom in legal_moves else BLUE
                else:
                    color = BLUE if dom in legal_moves else BLUE
                pygame.draw.rect(screen, color, rect)
                text = font.render(f"[{dom.highSide}/{dom.lowSide}]", True, WHITE)
                screen.blit(text, rect.topleft)

            pygame.display.flip()
        button_rects = []  # Clear button rects after selection
        return selected_domino

    def display_trump_popup(self):
        selected_trump = None
        running = True
        font = pygame.font.Font(None, 36)
        button_rects = []

        # Create buttons for trump selection (0-6)
        for i in range(7):
            button_rects.append(pygame.Rect(100 + i * 60, 300, 50, 50))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(event.pos):
                            selected_trump = i
                            running = False

            screen.fill(WHITE)

            # Draw buttons for trump selection
            for i, rect in enumerate(button_rects):
                pygame.draw.rect(screen, BLUE if rect.collidepoint(pygame.mouse.get_pos()) else RED, rect)
                text = font.render(str(i), True, WHITE)
                screen.blit(text, rect.topleft)

            pygame.display.flip()

        return selected_trump
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
        if not TEXT_INPUT:
            return self.display_bid_popup(current_bid)
        legalBid = False
        while (not legalBid):
            bid = int(input(f"{self.name}, enter your bid: "))
            if(current_bid > bid):
                
                print("Invalid bid, must be higher than the current bid.")
                print(f"Current bid is {current_bid}")
            else:
                legalBid = True
            
        return bid

    def display_bid_popup(self, current_bid):
        bid = 0
        running = True
        font = pygame.font.Font(None, 36)
        button_rects = []

        # Create buttons for bids
        for i in range(0, 43, 5):
            button_rects.append(pygame.Rect(100 + (i // 5) * 60, 300, 50, 50))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(event.pos):
                            bid = i * 5
                            running = False

            #screen.fill(WHITE)

            # Draw buttons
            for i, rect in enumerate(button_rects):
                pygame.draw.rect(screen, BLUE if rect.collidepoint(pygame.mouse.get_pos()) else RED, rect)
                text = font.render(str(i * 5), True, WHITE)
                screen.blit(text, rect.topleft)

            pygame.display.flip()

        return bid

class ComputerPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.suit_counts = [0] * 7  # Initialize suit counts

    def update_suit_counts(self):
        # Reset suit counts
        self.suit_counts = [0] * 7
        # Count the number of each suit in hand
        for domino in self.hand:
            self.suit_counts[domino.highSide] += 1
            self.suit_counts[domino.lowSide] += 1

    def play(self, dominoSet, playedDominos):
        print("Computer's turn, ", self.name)
        if(DEBUG):
            print("Computer's dominoes:")
            for dom in dominoSet:
                print("id:", dom.ID, "hi:", dom.highSide, "lo:", dom.lowSide, "double:", dom.isDouble)
        
        # Simple AI logic to select a domino to play
        selected_domino = self.select_domino(dominoSet)
        if selected_domino:
            self.hand.remove(selected_domino)
            # Draw the played domino on the screen
            self.draw_played_domino(selected_domino, playedDominos)
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
        if current_bid == 42:
            return 0

        # Update suit counts
        self.update_suit_counts()

        # Determine the bid based on suit counts
        max_suit_count = max(self.suit_counts)
        if max_suit_count == 7:
            bid = 42
        elif max_suit_count == 6:
            bid = random.randint(36, 38)
        elif max_suit_count == 5:
            bid = random.randint(33, 35)
        elif max_suit_count == 4:
            bid = random.randint(30, 32)
        else:
            bid = random.randint(0, 42)  # Simple AI for bidding

        # If calculated bid is less than current bid, pass (bid = 0)
        if bid < current_bid and bid < 30:
            bid = 0

        return bid

    def set_trump(self):
        # Set the trump based on the suit with the highest count
        self.update_suit_counts()
        self.trump = self.suit_counts.index(max(self.suit_counts))
        return self.trump
    
    def draw_played_domino(self, selected_domino, playedDominos):
        font = pygame.font.Font(None, 36)
        # Clear the middle area
        pygame.draw.rect(screen, WHITE, pygame.Rect(MIDDLE_X, MIDDLE_Y, 300, 200))

        # Draw played dominos
        for i, dom in enumerate(playedDominos):
            text = font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
            screen.blit(text, (MIDDLE_X + i * DOMINO_SPACING, MIDDLE_Y))

        # Draw the selected domino
        text = font.render(f"[{selected_domino.highSide}/{selected_domino.lowSide}]", True, BLACK)
        screen.blit(text, (MIDDLE_X + len(playedDominos) * DOMINO_SPACING, MIDDLE_Y))

        pygame.display.flip()

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
        self.font = pygame.font.Font(None, 25)  # Initialize font
        
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.state != GameState.QUIT:
                screen.fill(WHITE)

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
            elif self.state == GameState.QUIT:
                running = False

            self.draw_game_state()
            pygame.display.flip()

        
        pygame.quit()

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

        font = pygame.font.Font(None, 48)  # Font for the title

        for i in range(len(self.players)):
            player_index = (start_index + i) % len(self.players)
            player = self.players[player_index]

            # Draw the title "Bidding Phase"
            screen.fill(WHITE)
            text = font.render("Bidding Phase", True, BLACK)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
            pygame.display.flip()

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
        font = pygame.font.Font(None, 36)
        quit_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)

        while self.state == GameState.GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = GameState.QUIT
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        self.state = GameState.QUIT

            # Draw the current game state
            self.draw_game_state()

            # Draw the quit button on top
            pygame.draw.rect(screen, RED if quit_button.collidepoint(pygame.mouse.get_pos()) else BLUE, quit_button)
            text = font.render("Quit", True, WHITE)
            screen.blit(text, (quit_button.x + 20, quit_button.y + 10))
            pygame.display.flip()
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
            self.trump = self.players[winner_index].display_trump_popup()
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
        playedDominos = []
        for x in range(0, 7):
            trick_order = []  # Temporary array to store the order of each domino played
            for _ in range(4):
                player = self.players[self.current_player_index]
                legal_moves = player.filter_legal_moves(player.hand, self.trick.trick[0] if self.trick.trick else None)
                domino = player.play(legal_moves, playedDominos)
                playedDominos.append(domino)
                print(f"{player.name} plays domino [{domino.highSide}/{domino.lowSide}][{domino.ID}]")
                self.trick.trick.append(domino)
                self.trick.playerIndex.append(self.current_player_index)
                trick_order.append(self.current_player_index)  # Store the player index
                self.current_player_index = (self.current_player_index + 1) % 4

                # Draw the current game state
                self.draw_game_state()
                pygame.display.flip()

                # Wait for a short period to show the played domino
                pygame.time.wait(500)  # Adjust this value to change the delay (500 milliseconds = 0.5 seconds)

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

            if winner_player_index == 0 or winner_player_index == 2:  # player 1 and 3, Team 1
                self.teamOneTricks.append(self.trick.trick.copy())
            else:  # player 2 and 4, Team 2
                self.teamTwoTricks.append(self.trick.trick.copy())
            self.trick.trick = []

            # Clear the middle area
            pygame.draw.rect(screen, WHITE, pygame.Rect(MIDDLE_X, MIDDLE_Y, 300, 200))

            # Draw the current teams' tricks
            self.draw_teams_tricks()
            playedDominos = []

        print(f"Final Scores - Team 1: {self.teamOneScore}, Team 2: {self.teamTwoScore}")
    



    def calculate_scores(self):
        # Calculate scores and determine the winner
        pass

    def draw_teams_tricks(self):
        screen.fill(WHITE)

        font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 48)

        # Draw Team 1's title
        text = title_font.render("Team 1", True, BLACK)
        screen.blit(text, (50, 10))

        # Draw Team 1's dominos on the left
        y_offset = 50
        for trick in self.teamOneTricks:
            for i, dom in enumerate(trick):
                text = self.font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
                screen.blit(text, (50 + i * 50, y_offset))  # Reduced horizontal spacing
            y_offset += 50  # Adjust spacing between tricks

        # Draw Team 2's title
        text = title_font.render("Team 2", True, BLACK)
        screen.blit(text, (screen_width - 250, 10))

        # Draw Team 2's dominos on the right
        y_offset = 50
        for trick in self.teamTwoTricks:
            for i, dom in enumerate(trick):
                text = self.font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
                screen.blit(text, (screen_width - 250 + i * 50, y_offset))  # Reduced horizontal spacing
            y_offset += 50  # Adjust spacing between tricks

        pygame.display.flip()
    
    def draw_game_state(self):
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import test_trick  # Import the test module
        unittest.main(module='test_trick', argv=[sys.argv[0]])  # Run unit tests
    else:
        TEXT_INPUT = False
        DEBUG = False
        game = Game()
        game.run()