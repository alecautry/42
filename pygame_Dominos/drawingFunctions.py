import pygame

GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def drawGridIron(passScreen):
    # color as a tuple
    green = (0,255,0)
    grass = (0, 205, 0)
    innerFieldColor = (5, 235, 255)
    cowboysColor = (0, 53, 248)
    eaglesColor = (0, 76, 84)

    
    # coordinates of top left corner
    x_cord = 100 
    y_cord = 200

    # length and width drawn away from top left corner
    length = 300
    width = 720
    # Draw the base field shape
    pygame.draw.rect(passScreen, green,[x_cord, y_cord, width, length])

    # Draw the inner field color
    pygame.draw.rect(passScreen, innerFieldColor, [x_cord + 60, y_cord, width - 120, length])
    # Draw the outline
    pygame.draw.rect(passScreen, (0,0,0),[x_cord, y_cord, width, length], 5)



def drawButton2(buttonScreen, gameMouse,x, y, buttonWidth, buttonHeight, buttonColor):
    buttonDark = (buttonColor[0]*0.8, buttonColor[1]*0.8, buttonColor[2]*0.8)
    if x <= gameMouse[0] <= x+buttonWidth and y <= gameMouse[1] <= y+buttonHeight: 
        pygame.draw.rect(buttonScreen,buttonColor,[x,y,buttonWidth,buttonHeight]) 
          
    else: 
        pygame.draw.rect(buttonScreen,buttonDark,[x,y,buttonWidth,buttonHeight])
    

def draw_domino(screen, x, y, number1, number2):
    scale = 75
    pygame.draw.rect(screen, BLACK, (x, y, scale*2, scale), 2)  # Domino border
    pygame.draw.line(screen, BLACK, (x + scale, y), (x + scale, y + scale), 2)  # Center line
    font = pygame.font.SysFont(None, scale)
    text1 = font.render(str(number1), True, BLACK)
    text2 = font.render(str(number2), True, BLACK)
    screen.blit(text1, (x + scale/2 - scale/5, y+scale/4))
    screen.blit(text2, (x + scale + scale/4, y + scale/4))

def draw_text(window, text, x, y, size=24, color=BLACK):
    font = pygame.font.SysFont(None, size)
    render_text = font.render(text, True, color)
    window.blit(render_text, (x, y))
    
def draw_Player_Dominos(screen, dominoList, resolution):
    for x in range(len(dominoList)):
        if(x == 0):
            draw_domino(screen, 100, resolution[1] - 200, dominoList[0].highSide, dominoList[0].lowSide)   # Example center domino
        elif(x == 1):
            draw_domino(screen, 275, resolution[1] - 200, dominoList[1].highSide, dominoList[1].lowSide)   # Example bottom player domino
        elif(x == 2):    
            draw_domino(screen, 450, resolution[1] - 200, dominoList[2].highSide, dominoList[2].lowSide)   # Example top player domino
        elif(x == 3):
            draw_domino(screen, 625, resolution[1] - 200, dominoList[3].highSide, dominoList[3].lowSide)   # Example right player domino
        elif(x == 4):
            draw_domino(screen, 200, resolution[1] - 100, dominoList[4].highSide, dominoList[4].lowSide)   # Example left player domino
        elif(x == 5):    
            draw_domino(screen, 375, resolution[1] - 100, dominoList[5].highSide, dominoList[5].lowSide)   # Example left player domino
        elif(x == 6):    
            draw_domino(screen, 550, resolution[1] - 100, dominoList[6].highSide, dominoList[6].lowSide)   # Example left player domino