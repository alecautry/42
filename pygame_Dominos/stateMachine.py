# This is a global class for a StateMachine
# The MIT License

# Copyright (c) 2014 - 2020 Tal Yarkoni, Alexander Neumann

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import pygame
from transitions import Machine
from drawingFunctions import *
import time


class THE_GAME(object):

    # define the states
    states = ['MainMenu', 'Setup', 'Bidding', 'PlayGame','GameOver', 'Quit']
    # screen resolution 
    res = (900,900) 
    

    def __init__(self, name) :
       
        self.name = name
    
        # Data to keep track of 
        self.team1Score = 0
        self.team2Score = 0
        self.Trump = -1
        self.mouse = -1
        self.mouseDown = False
        self.mouseUp = False


        # state variables to use
        self.isMainMenu = False
        self.isSetup = False
        self.isQuit = False
        self.isBidding = False        

        # initializing the constructor 
        pygame.init() 
  
        
  
        # opens up a window 
        self.screen = pygame.display.set_mode(THE_GAME.res) 

        # itnialize the state machine
        self.Machine = Machine(model=self, states=THE_GAME.states, initial="MainMenu")


        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        self.Machine.add_transition(trigger="startGame", source='MainMenu', dest='Setup',conditions=['create_mainMenu','getIsSetup'])
        self.Machine.add_transition(trigger="startGame", source='MainMenu', dest='Quit', conditions=['create_mainMenu','getIsQuit'])
   
        # Setup leads to bidding
        self.Machine.add_transition(trigger='doneDealing', source='Setup', dest='Bidding', before='ask_for_bids')

        # Move from Bidding to Playing the game
        self.Machine.add_transition('doneBidding','Bidding','PlayGame', after='start_playing_dominos')

        # Move from Playing the game to GameOver state
        self.Machine.add_transition('donePlaying','PlayGame', 'GameOver', after='game_is_over')


        # Global States
        self.Machine.add_transition('mainMenu','*','MainMenu')


    def create_mainMenu(self):
        startGame = -1
        quitGame = 0

        startGame = drawButton2(self.screen,self.mouse, 100, 100, 100, 100, BLACK, self.mouseUp)
        quitGame = drawButton2(self.screen,self.mouse, 600, 400, 100, 100, GREEN, self.mouseUp)
        if(quitGame == 1):
            self.isQuit = True
            return True
        elif(startGame == 1):
            self.isSetup = True
            return True
        else: # do nothing case
            return False

    
    def deal_and_shuffle(self):
        print("Shuffling the Dominos..")
        print("Dealing the Dominos..")
        return True
    
    def ask_for_bids(self):
        print("asking player 1 for a bid")
        print("asking Last player")
        return 99
    
    def start_playing_dominos(self):
        print("Playing a doimino [4|4]")
        return 99
    
    def game_is_over(self):
        print("The human wins!")
        return 99



    # Simple getter functions for vairables
    def getIsQuit(self):
        return self.isQuit
    
    def getIsSetup(self):
        return self.isSetup

menu = 0
theGame = THE_GAME("42")
theGame.state
exit = False
clock = pygame.time.Clock()
clock.tick(60)
while(not exit):
    
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            theGame.mouseDown = True
        else:
            theGame.mouseDown = False
        if ev.type == pygame.MOUSEBUTTONUP:
            theGame.mouseUp = True
        else:
            theGame.mouseUp = False

    
    # fills the screen with a color every loop
    theGame.screen.fill((100,100,70))
    theGame.mouse = pygame.mouse.get_pos()

    if(theGame.state == 'MainMenu'):
        theGame.startGame()
    elif(theGame.state == 'Setup'):
        print("setup")
    elif(theGame.state == "Bidding"):
        print("Bidding")
    elif(theGame.state == 'Quit'):
        pygame.quit()
    else:
        exit = True

     

    # updates the frames of the game 
    pygame.display.update()
    #pygame.display.flip()

#clean up
pygame.quit()

