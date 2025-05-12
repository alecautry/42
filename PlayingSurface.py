from Surface import Surface
from constants import DOMINO_SPACING_X, DOMINO_WIDTH, DOMINO_HEIGHT, MIDDLE_X, MIDDLE_Y
import pygame

class PlayingSurface(Surface):
    def draw(self, trick):
        self.clear()  # Use the clear method to clear the surface
        for i, dom in enumerate(trick):
            image_path = f"assets/domino_{dom.ID}_{dom.highSide}_{dom.lowSide}.png"
            image = pygame.image.load(image_path)
            x = i * DOMINO_SPACING_X
            y = 0
            self.surface.blit(image, (x, y))

    def draw_played_domino(self, current_domino, player_index):
        font = pygame.font.Font(None, 36)

        # Draw the current domino in the correct player position
        positions = [
            (MIDDLE_X - DOMINO_WIDTH // 2, MIDDLE_Y),  # Player 1 (Left)
            (MIDDLE_X, MIDDLE_Y - DOMINO_HEIGHT // 2),  # Player 2 (Centered above)
            (MIDDLE_X + DOMINO_WIDTH // 2, MIDDLE_Y),  # Player 3 (Right)
            (MIDDLE_X, MIDDLE_Y + DOMINO_HEIGHT // 2)   # Player 4 (Centered below)
        ]
        x, y = positions[player_index]
        image_path = f"assets/domino_{current_domino.ID}_{current_domino.highSide}_{current_domino.lowSide}.png"
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (DOMINO_WIDTH, DOMINO_HEIGHT))  # Scale the image
        self.surface.blit(image, (x, y))

        pygame.display.flip()

    def clear(self):
        self.fill((0, 0, 0, 0))  # Use the fill method to clear the surface