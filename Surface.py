import pygame

class Surface:
    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

    def fill(self, color):
        self.surface.fill(color)

    def draw(self):
        raise NotImplementedError("Subclasses should implement this method")
