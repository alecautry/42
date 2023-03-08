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
    elif (dlead_high == (d3 & high) and (dlead_high == (d3 & low)): # If dlead mathces d3
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
    
