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
    pygame.draw.rect(screen, BLACK, (x, y, 50, 100), 2)  # Domino border
    pygame.draw.line(screen, BLACK, (x, y + 50), (x + 50, y + 50), 2)  # Center line
    font = pygame.font.SysFont(None, 24)
    text1 = font.render(str(number1), True, BLACK)
    text2 = font.render(str(number2), True, BLACK)
    screen.blit(text1, (x + 15, y + 15))
    screen.blit(text2, (x + 15, y + 65))

def draw_text(window, text, x, y, size=24, color=BLACK):
    font = pygame.font.SysFont(None, size)
    render_text = font.render(text, True, color)
    window.blit(render_text, (x, y))
    