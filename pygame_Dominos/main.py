import pygame
import sys
from functions import * # This will import all functions defined in "functions.py"
# Initialize the constructor
pygame.init()


# constants
resolution = (720,720)
# Creating the game Canvas
screen = pygame.display.set_mode(resolution)


width = screen.get_width()
height = screen.get_height()
color = (255,255,255) #white
color_light = (170,170,170) # lighter
color_dark = (100,100,100) # darker
rect_color = (255,0,0)
position = (0,0)

#Define system font
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, color)





# Title of Canvas
pygame.display.set_caption("My Table")

image = pygame.image.load("..\\table.png")



while True:  # Runs till exit is called

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        
        #check if mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
    
    # fills the screen with a color
    screen.fill((60,25,60))

    # Stores the (x,y) coorindates into the variables as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovering on a button change to lighter color
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
    
    # Superimposing the text onto our button
    screen.blit(text, (width/2+50, height/2))

    #updated the frames
    pygame.display.update()
