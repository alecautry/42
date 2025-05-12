import random
import pygame
from player import HumanPlayer, ComputerPlayer
from trick import Trick
from button import Button
from constants import *
from pygame_Dominos.domino import *
from SurfaceManager import SurfaceManager

class Game:
    def __init__(self):
        self.state = GameState.MAIN_MENU
        self.players = [HumanPlayer("Player 1", 0), ComputerPlayer("Player 2", 1), ComputerPlayer("Player 3", 2), ComputerPlayer("Player 4", 3)]
        self.trick = Trick()
        self.teamOneTricks = []
        self.teamTwoTricks = []
        self.dominoSet = []
        self.trump = None
        self.teamOneScore = 0
        self.teamTwoScore = 0
        self.font = pygame.font.Font(None, 25)  # Initialize font
        self.click = False
        self.surfaceManager = SurfaceManager(screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            
            if self.state != GameState.QUIT:
                #screen.fill((0, 0, 0, 0))
                pass
            
            if self.state == GameState.MAIN_MENU:
                self.main_menu()

            if self.state == GameState.INIT:
                self.initialize_game()
                self.state = GameState.BID

            elif self.state == GameState.BID:
                self.bidding_phase()
                self.state = GameState.PLAYING

            elif self.state == GameState.PLAYING:
                running = False
                #self.playing_phase()
                #self.state = GameState.GAME_OVER

            elif self.state == GameState.GAME_OVER:
                self.game_over()
            elif self.state == GameState.QUIT:
                running = False

            #self.draw_ui_elements()
            self.surfaceManager.draw_all(
                self.players[self.current_player_index].hand,
                self.trick.trick,
                self.teamOneScore,
                self.teamTwoScore
            )
            pygame.display.flip()

        
        pygame.quit()

    def draw_ui_elements(self):
        # Drawing logic for UI elements
        self.surfaceManager.uiSurface.draw(self.teamOneScore, self.teamTwoScore)
        screen.blit(self.surfaceManager.uiSurface.surface, (0, 0))

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)


    def main_menu(self):
        running = True
        while running:
            screen.fill((0,0,0))

            self.draw_text("42 Domino Game", self.font, (255, 255, 255), screen, screen_width // 2, 100)

            mx, my = pygame.mouse.get_pos()
            button_start = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
            button_quit = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)

            if button_start.collidepoint((mx, my)):
                if self.click:
                    self.state = GameState.INIT
                    running = False
            if button_quit.collidepoint((mx, my)):
                if self.click:
                    self.state = GameState.QUIT
                    running = False
            
            pygame.draw.rect(screen, (0, 0 ,255), button_start)
            self.draw_text('Start', self.font, (255, 255, 255), screen, screen_width // 2, screen_height // 2 - 25)
            pygame.draw.rect(screen, (255, 0 , 0), button_quit)
            self.draw_text('Quit', self.font, (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 75)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
            
            pygame.display.update()


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
            # screen.fill(WHITE, pygame.Rect(0, 0, screen_width, 100))
            text = font.render("Bidding Phase", True, BLACK)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
            
            # Draw the human player's hand
            if isinstance(player, HumanPlayer):
                player.draw_hand()

            bid = player.get_bid(bid)
            bids.append(bid)
            print(f"{player.name} bids {bid}")
            pygame.display.flip()

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
            self.draw_ui_elements()

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
        
        for x in range(0, 7):
            playedDominos = []
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

                # Draw the played domino on the screen
                self.surfaceManager.playingSurface.draw_played_domino(domino, self.trick.playerIndex[-1])

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
            # pygame.draw.rect(screen, WHITE, pygame.Rect(MIDDLE_X-150, MIDDLE_Y-100, 500, 250))
            pygame.display.flip()
            # Draw the current teams' tricks
            self.draw_teams_tricks()
            pygame.display.flip()
            playedDominos = []

        print(f"Final Scores - Team 1: {self.teamOneScore}, Team 2: {self.teamTwoScore}")
    



    def calculate_scores(self):
        # Calculate scores and determine the winner
        pass

    def draw_teams_tricks(self):
        font = pygame.font.Font(None, 36)

        # Draw Team 1's dominos on the left
        y_offset = 50
        for trick in self.teamOneTricks:
            for i, dom in enumerate(trick):
                text = self.font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
                screen.blit(text, (50 + i * 50, y_offset))  # Reduced horizontal spacing
            y_offset += 50  # Adjust spacing between tricks

        # Draw Team 2's dominos on the right
        y_offset = 50
        for trick in self.teamTwoTricks:
            for i, dom in enumerate(trick):
                text = self.font.render(f"[{dom.highSide}/{dom.lowSide}]", True, BLACK)
                screen.blit(text, (screen_width - 250 + i * 50, y_offset))  # Reduced horizontal spacing
            y_offset += 50  # Adjust spacing between tricks