import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 1920  # Updated width
screen_height = 1080 # Updated height
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

# Define scale factor based on screen width and height
SCALE_FACTOR_X = screen_width / 1920
SCALE_FACTOR_Y = screen_height / 1080

# Define standard coordinates for drawing dominos in the middle of the screen
MIDDLE_X_HAND = int(150 * SCALE_FACTOR_X)
MIDDLE_X = int(500 * SCALE_FACTOR_X)
MIDDLE_Y = int(1000 * SCALE_FACTOR_Y)
DOMINO_WIDTH = int(147 * SCALE_FACTOR_X)
DOMINO_HEIGHT = int(67 * SCALE_FACTOR_Y)
DOMINO_SPACING_X = int(157 * SCALE_FACTOR_X)
DOMINO_SPACING_Y = int(77 * SCALE_FACTOR_Y)

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
