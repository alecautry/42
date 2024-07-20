import pygame 
import sys 
from drawingFunctions import *
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (900,900) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
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
text = smallfont.render('quit' , True , color) 

# create football object from .bmp
football = pygame.image.load("Football-icon.bmp")
football.convert()

def drawButton():
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 

 

while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                  
    # fills the screen with a color every loop
    screen.fill((100,100,100)) 

    # Draw a bmp 
    screen.blit(football, (0, 360))
    
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    drawGridIron(screen)
    drawButton()
    drawButton2(screen, mouse, 2, 2, 100, 50, (150,210,200))
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
    
    # updates the frames of the game 
    pygame.display.flip()