from Surface import Surface

class PlayingSurface(Surface):
    def draw(self, trick):
        self.surface.fill((255, 255, 255))  # Clear the surface
        # Drawing logic for playing area
        for dom in trick:
            # Draw each domino in the trick
            pass
