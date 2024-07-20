import pygame 
import sys 
from drawingFunctions import *
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (900,900) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
pygame.display.set_caption('Texas 42')
  
# Colors

color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
quitText = smallfont.render('quit' , True , color) 


def drawButton():
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 

running = True

while running: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                running = False
                  
    # fills the screen with a color every loop
    screen.fill((100,100,70)) 
    
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      

    ## CHATGPT Help
    # Draw player areas based on the image
    pygame.draw.rect(screen, WHITE, (20, 70, 100, 550))   # Left player hand
    pygame.draw.rect(screen, WHITE, (140, 20, 620, 100))  # Top player hand
    pygame.draw.rect(screen, WHITE, (res[0] - 120, 70, 100, 550))  # Right player hand
    pygame.draw.rect(screen, color_dark, (0, res[1] - 270, res[0], res[1]))  # Bottom player hand

    # Draw center playing area
    pygame.draw.rect(screen, WHITE, (350, 275, 100, 50))  # Center playing area

    # Draw dominoes (placeholders)
    draw_domino(screen, 375, 285, 6, 1)  # Example center domino
    draw_domino(screen, 100, 520, 6, 1)  # Example bottom player domino
    draw_domino(screen, 100, 40, 6, 1)   # Example top player domino
    draw_domino(screen, 740, 270, 6, 1)  # Example right player domino
    draw_domino(screen, 40, 270, 6, 1)   # Example left player domino
    
    # Draw game information
    draw_text(screen, "Player 1 Score: 10", 320, 470)
    draw_text(screen, "Player 2 Score: 8", 320, 110)
    draw_text(screen, "Player 3 Score: 12", 700, 620)
    draw_text(screen, "Player 4 Score: 7", 20, 620)



    # if mouse is hovered on a button it 
    # changes to lighter shade  
    #drawButton2(screen, mouse, 2, 2, 100, 50, (150,210,200))
    # superimposing the text onto our button 
    #screen.blit(quitText , (width/2+50,height/2)) 
    
    # updates the frames of the game 
    pygame.display.flip()

#clean up
pygame.quit()
sys.exit()