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
    states = ['MainMenu','InGameMenu', 'Setup', 'Bidding', 'SetTrump','PlayGame','GameOver', 'Quit']
    # screen resolution 
    res = (900,900) 
    

    def __init__(self, name) :
       
        self.name = name
    
        # Data to keep track of 42 Stuff
        self.team1Score = 0
        self.team2Score = 0
        self.Trump = -1
        self.player1Hand = [0,0,0,0,0,0,0]
        self.computer2Hand= [0,0,0,0,0,0,0]
        self.computer3Hand= [0,0,0,0,0,0,0]
        self.computer4Hand= [0,0,0,0,0,0,0]
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
        self.Machine.add_transition(trigger='doneDealing', source='Setup', dest='Bidding', after='ask_for_bids')

        # Set Trump after bidding commpletes TODO
        self.Machine.add_transition('doneBidding','Bidding','SetTrump')

        # Move from "SetTrump" to Playing the game TODO
        self.Machine.add_transition('doneSettingTrump','SetTrump','PlayGame', after='start_playing_dominos')

        # Move from Playing the game to GameOver state TODO
        self.Machine.add_transition('donePlaying','PlayGame', 'GameOver', after='game_is_over')


        # Global States
        self.Machine.add_transition('mainMenu','*','MainMenu')

    # The Game State Functions
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
        print(self.computer2Hand[0].ID)

    # --- State Methods ---
    def askComputerBid(self, computerHand, curerntWinner): # TODO
        # Look at dominos
        # do fancy look up
        # determine possible bid
        # compare value to current vid
        print(computerHand[0].ID)
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
        return 0

    def askHumanBid(self, humanHand, currentMaxBid): # TODO - 
        # create a pop up
        asking = True
        humanBid = 0
        draw_Player_Bid(self.screen)
        asking = False
        # ask for a number above 29 or current max mid else pass


        # debug 
        humanBid = 30
        return humanBid, asking
    
    def setTrump(self, dominoArray, trump):
        for each in dominoArray:
            if(each.highSide == trump or (each.lowSide == trump)):
                each.isTrump = True
        
    def ask_for_bids(self): # TODO move the ask for bids function here. Instead of returns, update local class members
        asking = True
        currentWinner = [0,0] # [bidAmount, playerNum]
        currentBid = 0
        currentPlayer = self.startingPlayer
        allHands = [self.player1Hand, self.computer2Hand, self.computer3Hand, self.computer4Hand]
        # loop 4 times for all players
        for x in range(4):
            # reset starting player # for roll over
            if(currentPlayer == 4):
                currentPlayer = 0
        
            # if 2,3,4 its computer
            if(currentPlayer != 0):
                currentBid = self.askComputerBid(allHands[currentPlayer], currentWinner[0])
            # if 1, its human
            else:
                while(asking):
                    currentBid, asking = self.askHumanBid(allHands[0], currentWinner[0])

            #if the bid is better, then they win
            if(currentBid > currentWinner[0]):
                currentWinner[0] = currentBid
                currentWinner[1] = currentPlayer
        
            currentPlayer+=1
            currentBid = 0


        return currentWinner


    #this will return 1, 2, or 3. Which ever is the highest
    def compareFour(intOne: int, intTwo: int, intThree: int, intFour: int):
        if(intOne > intTwo):
            if(intOne > intThree):
                if(intOne > intFour):
                    return 1
                else:
                    return 4
            elif(intThree > intFour):
                return 3
            else:
                return 4
        elif(intTwo > intThree):
            if(intTwo > intFour):
                return 2
            else:
                return 4
        elif(intThree > intFour):
            return 3
        else:
            return 4

    def compareThree(intOne: int, intTwo: int, intThree: int) -> int:
        if( intOne > intTwo):
            if(intOne > intThree):
                return 1
            else:
                return 3
        elif (intTwo > intThree):
            return 2
        else:
            return 3

    def trickWinner(self, theTrick): # TODO
        #  trickWinner2(d1: DOMINO, d2: DOMINO, d3: DOMINO, d4: DOMINO) -> int:
        # dlead = d1
        d1 = theTrick[0]
        d2 = theTrick[1]
        d3 = theTrick[2]
        d4 = theTrick[3]

        if(d1.isTrump & d1.isDouble):
            return 1
        elif(d2.isTrump & d2.isDouble):
            return 2
        elif(d3.isTrump & d3.isDouble):
            return 3
        elif(d4.isTrump & d4.isDouble):
            return 4

        #if all trump compare ID
        if(d1.isTrump and d2.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, d2.ID, d3.ID, d4.ID)
        #if d4 isn't trump
        elif(d1.isTrump and d2.isTrump and d3.isTrump):
            return self.compareThree(d1.ID, d2.ID, d3.ID)
        #if d3 isn't trump
        elif(d1.isTrump and d2.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, d2.ID, -1, d4.ID)
        #if d2 isn't trump
        elif(d1.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, -1, d3.ID, d4.ID)
        #if d1 isn't trump
        elif(d2.isTrump and d3.isTrump and d4.isTrump):
            return self.compareFour(-1, d2.ID, d3.ID, d4.ID)
        #if d1 and d2
        elif(d1.isTrump and d2.isTrump):
            return self.compareTwo(d1.ID, d2.ID)
        #if d1 and d3
        elif(d1.isTrump and d3.isTrump):
            return self.compareThree(d1.ID , -1, d3.ID)
        #if d1 and d4
        elif(d1.isTrump and d4.isTrump):
            return self.compareFour(d1.ID, -1,-1, d4.ID)
        #if d2 and d3
        elif(d2.isTrump and d3.isTrump):
            return self.compareFour(-1,d2.ID,d3.ID,-1)
        #if d2 and d4
        elif(d2.isTrump and d4.isTrump):
            return self.compareFour(-1,d2.ID,-1,d4.ID)
        #if d3 and d4
        elif(d3.isTrump and d4.isTrump):
            return self.compareFour(-1,-1,d3.ID,d4.isTrump)
        elif(d1.isTrump):
            return 1
        elif(d2.isTrump):
            return 2
        elif(d3.isTrump):
            return 3
        elif(d4.isTrump):
            return 4

        # At this point we have no Trump
        # d1 is always lead
        if(d1.isDouble):
            return 1
        # if d2 is a double and matches the high side of d2 lead it is the highest double 
        elif d2.isDouble and (d2.highSide == d1.highSide): 
            return 2
        elif d3.isDouble and (d3.highSide == d1.highSide):
            return 3
        elif d4.isDouble and (d4.highSide == d1.highSide):
            return 4

        # No doubles matching Lead suit
        # Compare highside and ID
        if((d2.highSide == d1.highSide) and (d3.highSide == d1.highSide) and (d4.highSide == d1.highSide)):
            return compareFour(d1.ID, d2.ID, d3.ID, d4.ID) 
        #now compare 3
        # if 1, 2, and 3 have highside but not 4
        elif((d2.highSide == d1.highSide) and (d3.highSide == d1.highSide)):
            return compareFour(d1.ID, d2.ID, d3.ID, -1) 
        # if 1, 2, and 4 have highside but not 3
        elif((d2.highSide == d1.highSide) and (d4.highSide == d1.highSide)):
            return compareFour(d1.ID, d2.ID, -1, d4.ID) 
        # if 1 and 2 but not 3 and 4
        elif(d2.highSide == d1.highSide):
            return compareFour(d1.ID, d2.ID, -1, -1)
        # if 1 and 3 but not 2 and 4
        elif(d3.highSide == d1.highSide):
            return compareFour(d1.ID, -1, d3.ID, -1)
        # if 1 and 4 but not 2 and 3
        elif(d4.highSide == d1.highSide):
            return compareFour(d1.ID, -1, -1, d4.ID)

        # I think this is everything?
        # if nothing matches, return 1
        return 1

    #this will return 1 or 2. Which ever is highest
    def compareTwo(intOne: int, intTwo: int) -> int:
        if (intOne > intTwo):
            return 1
        else:
            return 2

    def start_playing_dominos(self):
        # Bid Winner sets trump

        return 99
    
    def game_is_over(self):
        print("The human wins!")
        return 99

    # --- pygame functions ---
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

    #  --- Simple getter functions for vairables ---
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
    print(theGame.state)

    if(theGame.state == 'MainMenu'):
        theGame.startGame()
    elif(theGame.state == 'Setup'):
        theGame.deal_and_shuffle() # this should be called from "doneDealing()"
        theGame.doneDealing()
    elif(theGame.state == "Bidding"):
        theGame.doneBidding()
    elif(theGame.state == "SetTrump"):
        theGame.doneSettingTrump()
    elif(theGame.state  == "PlayGame"):
        theGame.donePlaying()
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
