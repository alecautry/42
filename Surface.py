import pygame

class Surface:
    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height))

    def draw(self):
        raise NotImplementedError("Subclasses should implement this method")
