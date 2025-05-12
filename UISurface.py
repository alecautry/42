import pygame
from Surface import Surface

class UISurface(Surface):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background_image = pygame.image.load("assets/Background.png")
        self.background_image = pygame.transform.scale(self.background_image, (width, height))

    def draw(self, teamOneScore, teamTwoScore):
        # Draw background
        self.surface.blit(self.background_image, (0, 0))

        # Draw Team 1's title
        title_font = pygame.font.Font(None, 48)
        text = title_font.render("Team 1", True, (0, 0, 0))  # Black color
        self.surface.blit(text, (50, 10))

        # Draw Team 2's title
        text = title_font.render("Team 2", True, (0, 0, 0))  # Black color
        self.surface.blit(text, (self.surface.get_width() - 250, 10))

        # Draw team scores
        score_font = pygame.font.Font(None, 36)
        team_one_score_text = score_font.render(f"Score: {teamOneScore}", True, (0, 0, 0))
        team_two_score_text = score_font.render(f"Score: {teamTwoScore}", True, (0, 0, 0))
        self.surface.blit(team_one_score_text, (50, 60))
        self.surface.blit(team_two_score_text, (self.surface.get_width() - 250, 60))

    def clear(self):
        self.surface.fill((0, 0, 0, 0))
