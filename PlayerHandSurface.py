from Surface import Surface
from constants import DOMINO_SPACING_X, DOMINO_SPACING_Y
import pygame

class PlayerHandSurface(Surface):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background_image = pygame.image.load("assets/PlayerHandArea.png")

    def clear(self):
        self.fill((0, 0, 0, 0))  # Use the fill method to clear the surface

    def draw(self, hand):
        self.clear()  # Use the clear method to clear the surface
        for i, dom in enumerate(hand):
            image_path = f"assets/domino_{dom.ID}_{dom.highSide}_{dom.lowSide}.png"
            image = pygame.image.load(image_path)
            row = i // 4
            col = i % 4
            x = col * DOMINO_SPACING_X
            y = row * DOMINO_SPACING_Y
            self.surface.blit(image, (x, y))
