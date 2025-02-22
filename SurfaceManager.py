from PlayerHandSurface import PlayerHandSurface
from PlayingSurface import PlayingSurface
from UISurface import UISurface

class SurfaceManager:
    def __init__(self, screen):
        self.screen = screen
        self.playerHandSurface = PlayerHandSurface(800, 200)
        self.playingSurface = PlayingSurface(800, 400)
        self.uiSurface = UISurface(800, 100)

    def draw_all(self, hand, trick, teamOneScore, teamTwoScore):
        self.playerHandSurface.draw(hand)
        self.playingSurface.draw(trick)
        self.uiSurface.draw(teamOneScore, teamTwoScore)

        self.screen.blit(self.uiSurface.surface, (0, 0))
        self.screen.blit(self.playingSurface.surface, (0, 100))
        self.screen.blit(self.playerHandSurface.surface, (0, 500))
