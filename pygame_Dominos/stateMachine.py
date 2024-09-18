# This is a global class for a StateMachine

import pygame
from transitions import Machine
from pygame_Dominos.archive.functions import *
from drawingFunctions import *
from pygame_Dominos.domino import *
import random


class THE_GAME(object):
    # Create Class Variables that are constant to all classes
    # create all Dominos
    allDominos = DominoFactory.create()
    # define the states
    states = ['MainMenu','InGameMenu', 'Setup', 'Bidding', 'SetTrump','PlayGame','GameOver', 'Quit']
    # screen resolution 
    res = (900,900) 
    # light shade of the button 
    color_light = (170,170,170) 
  
    # dark shade of the button 
    color_dark = (100,100,100) 

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
        for x in range(7):  # Each hand starts as the first 7 Dominos
            self.player1Hand[x] = THE_GAME.allDominos[x]
            self.computer2Hand[x] = THE_GAME.allDominos[x+7]
            self.computer3Hand[x] = THE_GAME.allDominos[x+14]
            self.computer4Hand[x] = THE_GAME.allDominos[x+21]
        
        self.shuffledDominos = THE_GAME.allDominos # I need to see if changing shuffled Dominos effects THE_GAME.allDominos TODO

        self.startingPlayer = random.randrange(0, 4) # randomly determine who starts(player 1 is Human)
       
        self.currentBidWinner = -1


        # state variables to use
        self.isMainMenu = False
        self.isSetup = False
        self.isQuit = False
        self.isBidding = False     
        self.isSetTrump = False
        self.isPlayGame = False
        self.isGameOver = False   
        self.isInGameMenu = False


        # pygame Stuff 
        self.mouse = -1
        self.mouseDown = False
        self.mouseUp = False

        # initializing the pygame constructor 
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        # Create customer surfaces
        self.GUI_surf = pygame.surface.Surface(THE_GAME.res)
        self.BID_surf = pygame.surface.Surface(THE_GAME.res)
  
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
        self.Machine.add_transition(trigger='doneDealing', source='Setup', dest='Bidding',before='deal_and_shuffle',conditions=['deal_and_shuffle','getIsBidding'])

        # Set Trump after bidding commpletes TODO
        self.Machine.add_transition(trigger='doneBidding',source='Bidding',dest='SetTrump',conditions=['ask_for_bids', 'getIsSetTrump'])

        # Move from "SetTrump" to Playing the game TODO
        self.Machine.add_transition(trigger='doneSettingTrump',source='SetTrump',dest='PlayGame', after='start_playing_Dominos', conditions=['set_trump','getIsPlayGame'])

        # Move from Playing the game to GameOver state TODO
        self.Machine.add_transition(trigger='donePlaying',source='PlayGame', dest='GameOver', after='game_is_over', conditions=['game_is_over','getIsGameOver'])
    


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
        # use this to shuffle the Dominos
        random.shuffle(self.shuffledDominos)

        # Deal
        for x in range(7):
            self.player1Hand[x] = self.shuffledDominos[x]
            self.computer2Hand[x] = self.shuffledDominos[x+7]
            self.computer3Hand[x] = self.shuffledDominos[x+14]
            self.computer4Hand[x] = self.shuffledDominos[x+21]
        
        self.isBidding = True
        return True

    # --- State Methods ---
    def askComputerBid(self, computerHand, curerntWinner): # TODO
        # Look at Dominos
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
        print('here')
        
        draw_Player_Bid(self.screen, self.BID_surf)
        
        asking = False
        # ask for a number above 29 or current max mid else pass


        # debug 
        humanBid = 30
        return humanBid, asking
    
    def set_trump(self):
        # ask for a trump
        self.trump = 1

        for each in self.player1Hand:
            if(each.highSide == self.trump or (each.lowSide == self.trump)):
                each.isTrump = True
        for each in self.computer2Hand:
            if(each.highSide == self.trump or (each.lowSide == self.trump)):
                each.isTrump = True
        for each in self.computer3Hand:
            if(each.highSide == self.trump or (each.lowSide == self.trump)):
                each.isTrump = True
        for each in self.computer4Hand:
            if(each.highSide == self.trump or (each.lowSide == self.trump)):
                each.isTrump = True
        self.isSetTrump = False
        self.isPlayGame = True
        return True
        
    def ask_for_bids(self): # TODO move the ask for bids function here. Instead of returns, update local class members
        asking = True
        currentWinner = [0,0] # [bidAmount, playerNum]
        currentBid = 0
        self.startingPlayer
        allHands = [self.player1Hand, self.computer2Hand, self.computer3Hand, self.computer4Hand]
        # loop 4 times for all players
        
        # reset starting player for roll over
        if(self.startingPlayer == 4):
            self.startingPlayer = 0
    
        # if 2,3,4 its computer
        if(self.startingPlayer != 0):
            currentBid = self.askComputerBid(allHands[self.startingPlayer], currentWinner[0])
            self.startingPlayer += 1
        # if 1, its human
        else:
            currentBid, asking = self.askHumanBid(allHands[0], currentWinner[0])
            if(asking):
                self.startingPlayer += 1
                

        #if the bid is better, then they win
        if(currentBid > currentWinner[0]):
            currentWinner[0] = currentBid
            currentWinner[1] = self.startingPlayer
    
        
        currentBid = 0


        self.currentBidWinner = currentWinner
        self.isBidding = False
        #self.isSetTrump = True
        return True

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
        #  trickWinner2(d1: Domino, d2: Domino, d3: Domino, d4: Domino) -> int:
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

    def start_playing_Dominos(self):
        # Bid Winner sets trump

        self.isSetTrump = False
        self.isGameOver = True
        return True
    
    def game_is_over(self):
        print("The human wins!")

        self.isGameOver = False
        self.isMainMenu = True
        return True

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

    def drawMainGame(self):
        # draw Dominos on screen TODO
         # Draw player areas based on the image
        pygame.draw.rect(self.screen, WHITE, (20, 70, 100, 550))   # Left player hand
        pygame.draw.rect(self.screen, WHITE, (140, 20, 620, 100))  # Top player hand
        pygame.draw.rect(self.screen, WHITE, (self.res[0] - 120, 70, 100, 550))  # Right player hand
        
        # Human Player Location
        pygame.draw.rect(self.screen, self.color_dark, (0, THE_GAME.res[1] - 270, THE_GAME.res[0], THE_GAME.res[1]))  # Bottom player hand
        pygame.draw.rect(self.screen, self.color_light, (20, THE_GAME.res[1] - 250, THE_GAME.res[0]-40, 250))  # Bottom player hand


        # Draw center playing area
        pygame.draw.rect(self.screen, WHITE, (350, 275, 100, 50))  # Center playing area

        # Draw Dominoes (placeholders)
        # draw_Domino(screen, 100, res[1] - 200, 6, 0)   # Example center Domino
        # draw_Domino(screen, 275, res[1] - 200, 6, 1)   # Example bottom player Domino
        # draw_Domino(screen, 450, res[1] - 200, 6, 2)   # Example top player Domino
        # draw_Domino(screen, 625, res[1] - 200, 6, 3)   # Example right player Domino
        # draw_Domino(screen, 200, res[1] - 100, 6, 4)   # Example left player Domino
        # draw_Domino(screen, 375, res[1] - 100, 6, 5)   # Example left player Domino
        # draw_Domino(screen, 550, res[1] - 100, 6, 6)   # Example left player Domino
        draw_Player_Dominos(self.screen, self.player1Hand, self.res)
        # Draw game information
        draw_text(self.screen, "Player 1 Score: 10", 320, 470)
        draw_text(self.screen, "Player 2 Score: 8", 320, 110)
        draw_text(self.screen, "Player 3 Score: 12", 700, 620)
        draw_text(self.screen, "Player 4 Score: 7", 20, 620)
    #  --- Simple getter functions for vairables ---
    def getIsQuit(self):
        return self.isQuit
    
    def getIsBidding(self):
        return self.isBidding

    def getIsSetup(self):
        return self.isSetup

    def getIsSetTrump(self):
        return self.isSetTrump

    def getIsPlayGame(self):
        return self.isPlayGame
    
    def getIsGameOver(self):
        return self.isGameOver
    
    def getIsMainMenu(self):
        return self.isMainMenu
    
    def getIsInGameMenu(self):
        return self.isInGameMenu
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
    if(theGame.state != 'MainMenu'):
        theGame.drawMainGame()
    
    if(theGame.state == 'MainMenu'):
        theGame.startGame()     
    elif(theGame.state == 'Setup'):
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

#clean up
pygame.quit()
############################################################################################################################################################
