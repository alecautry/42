from Surface import Surface

class PlayerHandSurface(Surface):
    def draw(self, hand):
        self.surface.fill((255, 255, 255))  # Clear the surface
        # Drawing logic for player's hand
        for i, dom in enumerate(hand):
            # Draw each domino in the hand
            # ...existing code...
            pass
