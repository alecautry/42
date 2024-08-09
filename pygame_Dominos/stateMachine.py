# This is a global class for a StateMachine

import pygame
from transitions import Machine
#from functions import *
from drawingFunctions import *
from dominoObject import *
import time
import random


class THE_GAME(object):

    # Create Class Variables that are constant to all classes
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
    # define the states
    states = ['MainMenu', 'Setup', 'Bidding', 'PlayGame','GameOver', 'Quit']
    # screen resolution 
    res = (900,900) 
    

    def __init__(self, name) :
       
        self.name = name
    
        # Data to keep track of 42 Stuff
        self.team1Score = 0
        self.team2Score = 0
        self.Trump = -1
           
        for x in range(7):  # Each hand starts as the first 7 dominos
            self.player1Hand[x] = THE_GAME.allDominos[x]
            self.computer2Hand[x] = THE_GAME.allDominos[x+7]
            self.computer3Hand[x] = THE_GAME.allDominos[x+14]
            self.computer4Hand[x] = THE_GAME.allDominos[x+21]
        
        self.shuffledDominos = THE_GAME.allDominos # I need to see if changing shuffled Dominos effects THE_GAME.allDominos TODO

        self.startingPlayer = random.randrange(1, 5) # randomly determine who starts(player 1 is Human)
       
        
        # pygame Stuff 
        self.mouse = -1
        self.mouseDown = False
        self.mouseUp = False

        # state variables to use
        self.isMainMenu = False
        self.isSetup = False
        self.isQuit = False
        self.isBidding = False        

        # initializing the pygame constructor 
        pygame.init() 
        clock = pygame.time.Clock()
        clock.tick(60)
        
  
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

    # State Functions
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
        # Shuffle
        # use this to shuffle the dominos
        random.shuffle(self.shuffledDominos)

        # Deal
        for x in range(7):
            self.player1Hand[x] = self.shuffledDominos[x]
            self.computer2Hand[x] = self.shuffledDominos[x+7]
            self.computer3Hand[x] = self.shuffledDominos[x+14]
            self.computer4Hand[x] = self.shuffledDominos[x+21]
        return True

    # Helper functions
    def askComputerBid(self, computerHand, curerntWinner):
        # Look at dominos
        # do fancy look up
        # determine possible bid
        # compare value to current vid
        suits = [0,0,0,0,0,0,0]
        # loop through each suit and determine how many of each you have
        for x in range(7):
            if(computerHand[x].lowSide == 0):
                suits[0] += 1
            if(computerHand[x].lowSide == 1 or computerHand[x].highSide == 1):
                suits[1] += 1
            if(computerHand[x].lowSide == 2 or computerHand[x].highSide == 2):
                suits[2] += 1
            if(computerHand[x].lowSide == 3 or computerHand[x].highSide == 3):
                suits[3] += 1
            if(computerHand[x].lowSide == 4 or computerHand[x].highSide == 4):
                suits[4] += 1
            if(computerHand[x].lowSide == 5 or computerHand[x].highSide == 5):
                suits[5] += 1
            if(computerHand[x].lowSide == 6 or computerHand[x].highSide == 6):
                suits[6] += 1
        print(suits)

    def askHumanBid(self):
        print("here")
    

    def ask_for_bids(self): # TODO move the ask for bids function here. Instead of returns, update local class members
        asking = True
        currentWinner = [0,0] # [bidAmount, playerNum]
        currentBid = 0
        currentPlayer = self.startingPlayer
        allHands = [self.player1Hand, self.computer2Hand, self.computer3Hand, self.computer4Hand]
        # loop 4 times for all players
        for x in range(4):
            # reset starting player # for roll over
            if(currentPlayer == 5):
                currentPlayer = 1
        
            # if 2,3,4 its computer
            if(currentPlayer != 1):
                currentBid = THE_GAME.askComputerBid(allHands[currentPlayer], currentWinner[0])
            # if 1, its human
            else:
                while(asking):
                    currentBid, asking = THE_GAME.askHumanBid(allHands[0], currentWinner[0])

            #if the bid is better, then they win
            if(currentBid > currentWinner[0]):
                currentWinner[0] = currentBid
                currentWinner[1] = currentPlayer
        
            currentPlayer+=1
            currentBid = 0


        return currentWinner

    
    def start_playing_dominos(self):
        print("Playing a doimino [4|4]")
        return 99
    
    def game_is_over(self):
        print("The human wins!")
        return 99

    


    # pygame functions
    def updatePygame(self):
        
        #static updates
        theGame.mouse = pygame.mouse.get_pos()

    
    def eventUpdate(self):
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

    # Simple getter functions for vairables
    def getIsQuit(self):
        return self.isQuit
    
    def getIsSetup(self):
        return self.isSetup

# end of Class




# move this to main.py later
########################################################################################################################################################
theGame = THE_GAME("42")
exit = False

while(not exit):
    # check for events
    theGame.eventUpdate()

    #update static varibales
    theGame.updatePygame()
        
    
    # fills the screen with a color every loop
    theGame.screen.fill((100,100,70))
    

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
############################################################################################################################################################
