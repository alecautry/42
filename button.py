import pygame


class Button:
    def __init__(self, x, y, width, height, text, font, bg_color, text_color, highlight_color=None, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.highlight_color = highlight_color
        self.image = image

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.highlight_color and self.rect.collidepoint(mouse_pos):
            color = self.highlight_color
        else:
            color = self.bg_color

        pygame.draw.rect(screen, color, self.rect)

        if self.image:
            # Draw sprite centered in the button
            img_rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, img_rect)
        else:
            # Draw text if no sprite
            text_surface = self.font.render(self.text, True, self.text_color)
            screen.blit(
                text_surface, 
                (
                    self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                    self.rect.y + (self.rect.height - text_surface.get_height()) // 2
                )
            )

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)
