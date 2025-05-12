from PlayerHandSurface import PlayerHandSurface
from PlayingSurface import PlayingSurface
from UISurface import UISurface
from Surface import Surface
from constants import DOMINO_SPACING_X, DOMINO_WIDTH, DOMINO_HEIGHT, MIDDLE_X, MIDDLE_Y
import pygame

class SurfaceManager:
    def __init__(self, screen):
        self.screen = screen
        self.playerHandSurface = PlayerHandSurface(1920, 200)  # Updated width
        self.playingSurface = PlayingSurface(1920, 680)        # Updated width and height
        self.uiSurface = UISurface(1920, 1080)                 # Updated width and height

    def draw_all(self, hand, trick, teamOneScore, teamTwoScore):
        self.draw_player_hand(hand)
        self.draw_playing_area(trick)
        self.draw_ui(teamOneScore, teamTwoScore)

    def draw_player_hand(self, hand):
        self.playerHandSurface.draw(hand)
        self.screen.blit(self.playerHandSurface.surface, (0, 880))

    def draw_playing_area(self, trick):
        self.playingSurface.draw(trick)
        self.screen.blit(self.playingSurface.surface, (0, 200))

    def draw_ui(self, teamOneScore, teamTwoScore):
        self.uiSurface.draw(teamOneScore, teamTwoScore)
        self.screen.blit(self.uiSurface.surface, (0, 0))

    def clear(self):
        self.fill((0, 0, 0, 0))  # Use the fill method to clear the surface
