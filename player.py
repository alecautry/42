import pygame
import random
import sys
from button import Button
from constants import *
from PlayerHandSurface import PlayerHandSurface

TEXT_INPUT = False
class HumanPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hand = []
        self.playerHandSurface = PlayerHandSurface(1920, 200)  # Initialize PlayerHandSurface

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


        return selected_domino

    def display_play_popup(self, dominoSet, playedDominos):
        selected_domino = None
        running = True
        font = pygame.font.Font(None, 36)
        button_rects = []

        # Create buttons for legal dominos in hand
        for i, dom in enumerate(self.hand):
            image_path = f"assets/domino_{dom.ID}_{dom.highSide}_{dom.lowSide}.png"
            image = pygame.image.load(image_path)
            row = i // 4
            col = i % 4
            x = MIDDLE_X_HAND + col * DOMINO_SPACING_X
            y = 600 + row * DOMINO_SPACING_Y  # Adjusted y-coordinate to draw lower on the screen
            if dom in dominoSet:
                button = Button(
                    x, y, DOMINO_WIDTH, DOMINO_HEIGHT,
                    "", font, BLUE, WHITE, highlight_color=RED, image=image
                )
                button_rects.append((button, dom))
            else:
                screen.blit(image, (x, y))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button, dom in button_rects:
                        if button.collidepoint(event.pos):
                            selected_domino = dom
                            running = False

            # Clear the hand area using the clear method
            self.playerHandSurface.clear()

            # Draw all dominos in hand
            for button, dom in button_rects:
                button.draw(screen)

            pygame.display.flip()
        button_rects = []  # Clear button rects after selection
        self.hand.remove(selected_domino)  # Remove the selected domino from the player's hand
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

            #screen.fill(WHITE)

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

        pass_button = Button(100, 300, 80, 50, "Pass", font, RED, WHITE, highlight_color=GREEN)
        up_button = Button(200, 300, 80, 50, "Up", font, RED, WHITE, highlight_color=GREEN)
        down_button = Button(300, 300, 80, 50, "Down", font, RED, WHITE, highlight_color=GREEN)
        enter_button = Button(400, 300, 80, 50, "Enter", font, RED, WHITE, highlight_color=GREEN)

        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pass_button.collidepoint(event.pos):
                        bid = 0
                        running = False
                    elif up_button.collidepoint(event.pos):
                        if bid == 0:
                            bid = 30
                        elif 30 <= bid < 42:
                            bid += 1
                    elif down_button.collidepoint(event.pos):
                        if 31 <= bid <= 42:
                            bid -= 1
                        elif bid == 30:
                            bid = 0
                    elif enter_button.collidepoint(event.pos):
                        running = False

            self.playerHandSurface.clear()  # Use the clear method

            self.draw_hand()
            pass_button.draw(screen)
            up_button.draw(screen)
            down_button.draw(screen)
            enter_button.draw(screen)
           

            bid_text = font.render(f"Current Bid: {bid}", True, BLACK)
            screen.blit(bid_text, (100, 250))

            pygame.display.flip()

        return bid

    def draw_hand(self):
        self.playerHandSurface.draw(self.hand)
        screen.blit(self.playerHandSurface.surface, (0, 1080))  # Adjusted y-coordinate to draw lower on the screen


class ComputerPlayer:
    def __init__(self, name, position):
        self.name = name
        self.hand = []
        self.position = position
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
