import pygame
from constants import *
from game import Game  # Import the Game class
from SurfaceManager import SurfaceManager

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("42 Domino Game")

debug = True

def run_test():
    print("Running test code...")
    surfaceManager = SurfaceManager(screen)
    teamOneScore = 0
    teamTwoScore = 0
    running = True
    color = (0, 0, 255)
    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    color = (255, 0, 0, 255)
                if event.key == pygame.K_RETURN:
                    color = (0, 255, 0, 255)
                if event.key == pygame.K_BACKSPACE:
                    color = (0, 0, 0, 0)


        #screen.fill((200, 200, 200))  # Clear the screen with black
        
        
        surfaceManager.draw_ui(teamOneScore, teamTwoScore)
        #surfaceManager.playingSurface.fill((255, 255, 255))
        surfaceManager.playerHandSurface.fill(color)
        surfaceManager.playingSurface.surface.set_alpha(1)

        screen.fill((0))
        screen.blit(surfaceManager.uiSurface.surface, (0, 0))
        #if(surfaceManager.playingSurface.surface.get_alpha() != 0):
        screen.blit(surfaceManager.playingSurface.surface, (0, 200))
        #screen.blit(surfaceManager.playingSurface.surface, (0, 200), special_flags=pygame.BLEND_RGBA_MAX)
        screen.blit(surfaceManager.playerHandSurface.surface, (0, 880))
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    if debug:
        run_test()
    else:
        game = Game()
        game.run()