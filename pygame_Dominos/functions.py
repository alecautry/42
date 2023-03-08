# Functions file to handle Trick winnings or anything else
# Pass in 4 dominos, starting with the lead, and the last 
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
    if dlead > d2 and (dlead > d3) and (dlead > d4):
        return dlead
    # if dlead not the highest, have to compare dlead high to both sides
    elif dlead_high == (d2 & high) or (dlead_high == (d2 * low)): # If dlead high is the same 
        return 2

    
    

# RULES OF 42 with Bit operations

# If double Trump
# If Trump and nothing else
# If highest trump

# If trump pick highest value domino 

# If double of leadSuit
# if dlead_high & dlead


# If highest of suit
# if only of suit
