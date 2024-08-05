# Functions file to handle Trick winnings or anything else
# Pass in 4 dominos, starting with the lead, and the last 
from dominoObject import *
from drawingFunctions import *
def trickWinner(dlead, d2, d3, d4):
    # Compare Dominos

    high = 0b00111111000000
    low = 0b00000000111111
    trump = 0b10000000000000
    double = 0b01000000000000




    dlead_high = dlead & high
    dlead_low = dlead & low
    dlead_trump = dlead & trump
    dlead_double = dlead & double

    if dlead_trump == trump and (dlead_double == double):  #this checks if a trump and double (Always wins)
        return dlead

    if dlead_trump == trump:  # If dlead trump and trump
        if(dlead > d2 and (dlead > d3) and (dlead > d4)): # Check if dlead is greater than everything else
            return dlead
    elif(d2 & trump == trump):  # Check if d2 is a trump
        if(d2 > d3 and (d2 > d4)): # Check if d2 is greater than d3 and d4
            return d2
    elif(d3 & trump == trump): # Check if d3 is trump
        if(d3 > d4): # Check if d3 is greater than d4
            return d4
    elif(d4 & trump == trump): # Check if d4 is trump
        return d4 # return d4 as it is the only trump 
    
    # No more trumps so now check for double
    if dlead_double == double:
        return dlead
    elif d2 & double == double and (d2 & high == dlead_high): # if d2 is a double and matches the high side of d2 lead it is the highest double 
        return d2
    elif d3 & double == double and (d3 & high == dlead_high):
        return d3
    elif d4 & double == double and (d4 & high == dlead_high):
        return d4
    
    # No double, no trumps, have to compare more dlead high
    # If dlead is highest it will always win
    if dlead > d2 and (dlead > d3) and (dlead > d4):
        return dlead
    # if dlead not the highest, have to compare dlead high to both sides
    elif dlead_high == (d2 & high) or (dlead_high == (d2 & low)): # If d2 matches dlead high
        if (dlead_high == (d3 & high)) or (dlead_high == (d3 & low)): # If d3 matches dlead high
            if (dlead_high == (d4 & high)) or (dlead_high == (d4 & low)): # If d4 matches dlead high
                # If all dominos share a lead rerturn the highest
                if dlead > d2 and (dlead > d3) and (dlead >d4):
                    return dlead
 
                elif d2 > d3 and (d2 > d4): # if not dlead, check d2
                    return d2
 
                elif d3 > d4: # if not d2, check d3
                    return d3
 
                else:   # has to be d4
                    return d4
 
            # If D4 doesn't match but dlead, d2 and d3 match
            elif dlead > d2 and (dlead > d3):
                return dlead
 
            elif d2 > d3:
                return d2
 
            else:
                return d3
        #If only d2 and dlead match
        elif dlead > d2:
        
            return dlead
        
        else:
            return d2
 
    #if d2 doesn't match
    elif (dlead_high == (d3 & high) and (dlead_high == (d3 & low))): # If dlead mathces d3
        if dlead_high == (d4 & high) and (dlead_high == (d4 & low)): # if dlead matched d4
            if dlead > d3 and (dlead > d4): # compare higher
                return dlead

            elif d3 > d4: # if not dlead then d3
                return d3
 
            else: # has to be d4
                return d4
 
        # if dlead only matches d3
        elif dlead > d3:
            return dlead
 
        else:
            return d3
    
    # if only d4 matches          
    elif dlead_high == (d4 & high) and (dlead_high == (d4 & low)):
        if dlead > d4:
            return dlead

        else:
            return d4

    # If nothing matches dlead then it walks (Wins) 
    else:
        return dlead 
    

def setTrump(dominoArray, trump):
    for each in dominoArray:
        if(each.highSide == trump or (each.lowSide == trump)):
            each.isTrump = True
        
def dealHands(humanPlayer, computerPlayer1, computerPlayer2, computerPlayer3, shuffledDominos):
    for x in range(7):
        humanPlayer[x] = shuffledDominos[x]
        computerPlayer1[x] = shuffledDominos[x+7]
        computerPlayer2[x] = shuffledDominos[x+14]
        computerPlayer3[x] = shuffledDominos[x+21]




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

#this will return 1 or 2. Which ever is highest
def compareTwo(intOne: int, intTwo: int) -> int:
    if (intOne > intTwo):
        return 1
    else:
        return 2
#return the int of who wins (1, 2, 3, 4)
def trickWinner2(d1: DOMINO, d2: DOMINO, d3: DOMINO, d4: DOMINO) -> int:
    dlead = d1

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
        return compareFour(d1.ID, d2.ID, d3.ID, d4.ID)
    #if d4 isn't trump
    elif(d1.isTrump and d2.isTrump and d3.isTrump):
        return compareThree(d1.ID, d2.ID, d3.ID)
    #if d3 isn't trump
    elif(d1.isTrump and d2.isTrump and d4.isTrump):
        return compareFour(d1.ID, d2.ID, -1, d4.ID)
    #if d2 isn't trump
    elif(d1.isTrump and d3.isTrump and d4.isTrump):
        return compareFour(d1.ID, -1, d3.ID, d4.ID)
    #if d1 isn't trump
    elif(d2.isTrump and d3.isTrump and d4.isTrump):
        return compareFour(-1, d2.ID, d3.ID, d4.ID)
    #if d1 and d2
    elif(d1.isTrump and d2.isTrump):
        return compareTwo(d1.ID, d2.ID)
    #if d1 and d3
    elif(d1.isTrump and d3.isTrump):
        return compareThree(d1.ID , -1, d3.ID)
    #if d1 and d4
    elif(d1.isTrump and d4.isTrump):
        return compareFour(d1.ID, -1,-1, d4.ID)
    #if d2 and d3
    elif(d2.isTrump and d3.isTrump):
        return compareFour(-1,d2.ID,d3.ID,-1)
    #if d2 and d4
    elif(d2.isTrump and d4.isTrump):
        return compareFour(-1,d2.ID,-1,d4.ID)
    #if d3 and d4
    elif(d3.isTrump and d4.isTrump):
        return compareFour(-1,-1,d3.ID,d4.isTrump)
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


def askComputerBid(computerHand, currentMaxBid, tablePosition)->int:
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

    return 0


def askHumanBid(screen, humanHand, currentMaxBid)->int:
    # create a pop up
    asking = True
    humanBid = 0
    draw_Player_Bid(screen)
    asking = False
    # ask for a number above 29 or current max mid else pass

    return humanBid, asking

def askForBids(screen, startingPlayer, allHands) -> list:
    
    asking = True
    currentWinner = [0,0] # [bidAmount, playerNum]
    currentBid = 0
    currentPlayer = startingPlayer
    # loop 4 times for all players
    for x in range(4):
        # reset starting player # for roll over
        if(currentPlayer == 5):
           currentPlayer = 1
        
        # if 2,3,4 its computer
        if(currentPlayer != 1):
            currentBid = askComputerBid(allHands[currentPlayer - 1], currentWinner[0], x)
        # if 1, its human
        else:
            while(asking):
                currentBid, asking = askHumanBid(screen, allHands[0], currentWinner[0])

        #if the bid is better, then they win
        if(currentBid > currentWinner[0]):
                currentWinner[0] = currentBid
                currentWinner[1] = currentPlayer
        
        currentPlayer+=1
        currentBid = 0


    return currentWinner