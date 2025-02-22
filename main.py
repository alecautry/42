
import pygame
from constants import *
from game import Game  # Import the Game class

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("42 Domino Game")

if __name__ == "__main__":
    game = Game()
    game.run()