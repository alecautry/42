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
GREEN = (0, 255, 0)
DARK_RED = (139, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Define standard coordinates for drawing dominos in the middle of the screen
MIDDLE_X_HAND = 150
MIDDLE_X = 350
MIDDLE_Y = 200
DOMINO_WIDTH = 147
DOMINO_HEIGHT = 67
DOMINO_SPACING_X = 157
DOMINO_SPACING_Y = 77

TEXT_INPUT = False
DEBUG = False

class GameState:
    # Main Menu
    MAIN_MENU = "MAIN_MENU"

    # Shuffle and deal dominoes
    INIT = "INIT"

    # Players place bids to determine who goes first
    BID = "BID"

    # Play the game: players take turns placing dominoes
    PLAYING = "PLAYING"

    # Game is over: calculate scores and determine winner
    GAME_OVER = "GAME_OVER"

    QUIT = "QUIT"
