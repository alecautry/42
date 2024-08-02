import pygame 
import sys
import random

from drawingFunctions import *
from dominoObject import *
from functions import *


  
# create all dominos
d0 = DOMINO(0,0,0,True,False) 
d1 = DOMINO(1,1,0,False,False)
d2 = DOMINO(2,1,1,True,False)
d3 = DOMINO(3,2,0,False,False)
d4 = DOMINO(4,2,1,False,False)
d5 = DOMINO(5,2,2,True,False)
d6 = DOMINO(6,3,0,False,False)
d7 = DOMINO(7,3,1,False,False)
d8 = DOMINO(8,3,2,False,False)
d9 = DOMINO(9,3,3,True,False)
d10 = DOMINO(10,4,0,False,False)
d11 = DOMINO(11,4,1,False,False)
d12 = DOMINO(12,4,2,False,False)
d13 = DOMINO(13,4,3,False,False)
d14 = DOMINO(14,4,4,True,False)
d15 = DOMINO(15,5,0,False,False)
d16 = DOMINO(16,5,1,False,False)
d17 = DOMINO(17,5,2,False,False)
d18 = DOMINO(18,5,3,False,False)
d19 = DOMINO(19,5,4,False,False)
d20 = DOMINO(20,5,5,True,False)
d21 = DOMINO(21,6,0,False,False)
d22 = DOMINO(22,6,1,False,False)
d23 = DOMINO(23,6,2,False,False)
d24 = DOMINO(24,6,3,False,False)
d25 = DOMINO(25,6,4,False,False)
d26 = DOMINO(26,6,5,False,False)
d27 = DOMINO(27,6,6,True,False)

allDominoIDs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
allDominos = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d27]
trump = 3
startingPlayer = 0


computerPlayer2 = [0,0,0,0,0,0,0]
computerPlayer3 = [0,0,0,0,0,0,0]
computerPlayer4 = [0,0,0,0,0,0,0]
humanPlayer = [0,0,0,0,0,0,0]





# use this funciton to set trump
setTrump(allDominos, trump)

# use this to shuffle the dominos
random.shuffle(allDominos)

# randomly determine who starts(player 1 is Human)

startingPlayer = random.randrange(1, 5)

# assign dominos to each players hands (Deal)
dealHands(humanPlayer, computerPlayer2, computerPlayer3, computerPlayer4, allDominos)

allHands = [humanPlayer, computerPlayer2, computerPlayer3, computerPlayer4]

# Draw hands
# draw_Player_Dominos(humanPlayer)
# Bidding (Determine likely bid for each computer hand, add a prompt for player (Use graphics!))
winningBid = (0,0)


winningBid = askForBids(startingPlayer, allHands)

# Winner Sets Trump



# Winner plays first domino (Have the computer players play first legal domino)

# show each Domino on the board (Some kind of turned based animation)

# wait for player to pick one (Myabe highlight what is legal)

# 




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

    # Human Player Location
    pygame.draw.rect(screen, color_dark, (0, res[1] - 270, res[0], res[1]))  # Bottom player hand
    pygame.draw.rect(screen, color_light, (20, res[1] - 250, res[0]-40, 250))  # Bottom player hand


    # Draw center playing area
    pygame.draw.rect(screen, WHITE, (350, 275, 100, 50))  # Center playing area

    # Draw dominoes (placeholders)
    # draw_domino(screen, 100, res[1] - 200, 6, 0)   # Example center domino
    # draw_domino(screen, 275, res[1] - 200, 6, 1)   # Example bottom player domino
    # draw_domino(screen, 450, res[1] - 200, 6, 2)   # Example top player domino
    # draw_domino(screen, 625, res[1] - 200, 6, 3)   # Example right player domino
    # draw_domino(screen, 200, res[1] - 100, 6, 4)   # Example left player domino
    # draw_domino(screen, 375, res[1] - 100, 6, 5)   # Example left player domino
    # draw_domino(screen, 550, res[1] - 100, 6, 6)   # Example left player domino
    draw_Player_Dominos(screen, humanPlayer, res)
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