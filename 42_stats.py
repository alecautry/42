from functions import *
import array as ar
from itertools import *
import time
import copy as cp
import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
start = time.time()

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

dominoData = [(0,0,0,True,False),
(1,1,0,False,False),
(2,1,1,True,False),
(3,2,0,False,False),
(4,2,1,False,False),
(5,2,2,True,False),
(6,3,0,False,False),
(7,3,1,False,False),
(8,3,2,False,False),
(9,3,3,True,False),
(10,4,0,False,False),
(11,4,1,False,False),
(12,4,2,False,False),
(13,4,3,False,False),
(14,4,4,True,False),
(15,5,0,False,False),
(16,5,1,False,False),
(17,5,2,False,False),
(18,5,3,False,False),
(19,5,4,False,False),
(20,5,5,True,False),
(21,6,0,False,False),
(22,6,1,False,False),
(23,6,2,False,False),
(24,6,3,False,False),
(25,6,4,False,False),
(26,6,5,False,False),
(27,6,6,True,False)]
dominoColumns = ["ID", "HighSide", "LowSide", "isDouble","isTrump"]

dominoRange = range(28)
allDominoIDs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
trumpRange = range(8)

allDominos = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d27]


combo = permutations(dominoRange, 4)


######################################################################

trickWinnerFile = Path("./trickWinner.parquet")
if not trickWinnerFile.is_file(): # if the file doesn't exist, create it, else, skip and just read
    giantArray = []
    start = time.time()
    field = ["trump","Dlead.ID", "d2.ID", "d3.ID", "d4.ID", "winner"]
    #trickWinnerDataFrame = pd.DataFrame(columns=field)
    
    # Create a check for 'trickWinner.parquet' and skip the code that doesn't need to ran
    for trumpITER in trumpRange:
        trump = trumpITER
        setTrump(allDominos, trump)
        #a = (0,1,2,3) a[0] = 0, a[1] = 1, 
        
        for a in combo:
            
            winner = trickWinner2(allDominos[a[0]], allDominos[a[1]], allDominos[a[2]], allDominos[a[3]])
            saveString = [(trump, allDominos[a[0]].ID, allDominos[a[1]].ID, allDominos[a[2]].ID, allDominos[a[3]].ID, winner)]
            giantArray.extend(saveString) # using extend is fast than append the '(' ')' are needed when using extend and converting to dataFrame
        
    end = time.time()
    print(end-start)
    dataFrame = pd.DataFrame(giantArray,columns=field)
    table1 = pa.Table.from_pandas(dataFrame)
    pq.write_table(table1, 'trickWinner.parquet')

table2 = pq.read_table('trickWinner.parquet')
dataFrame2 = table2.to_pandas()
giantArray2 = list(dataFrame2.itertuples(index=False, name=None)) # this may be uneseccary

# This will loop all games, WAY TOO MANY, but good reference code
fields = ["player1", "Player2", "Player3","player4"]
allGamesArray = []
saveString = list()

start = time.time()
player1hands = list(combinations(allDominoIDs,7))
tempDominoList = list(allDominoIDs)
# remove the dominos in player 1 hand from the list
for x in player1hands[0]:
    tempDominoList.remove(x)

##main loop: 
##create a list of all combos in regards to what 21 doms are left
it = 0 
player2hands = combinations(tempDominoList, 7)
for j in player2hands:
    
    jLoopStart = time.time()
    tempDominoList2 = tempDominoList[:]
    
    for y in range(7):
        #tempDominoList[tempDominoList.index(j[y])] = 0
        tempDominoList.remove(j[y])

   
    player3hands = combinations(tempDominoList, 7)
    
    for z in player3hands:
        it += 1
        tempDominoList3 = tempDominoList[:]
        for y in range(7):
            tempDominoList.remove(z[y])
        player4hand = tempDominoList
        
        
        saveString.extend(list(player1hands[0]))
        saveString.extend(list(j))
        saveString.extend(list(z))
        saveString.extend(list(player4hand))
        print(tuple(saveString))
        allGamesArray.extend([tuple(saveString)])
        saveString.clear()
        tempDominoList = tempDominoList3[:]
    tempDominoList = tempDominoList2[:]
    dataFrame = pd.DataFrame(allGamesArray, columns=range(28))
    print(dataFrame)
    print(dataFrame.info())
    table2 = pa.Table.from_pandas(allGamesArray, schema=pd.Int64Dtype)
    pq.write_table(table1, 'AllGameCombos%d.parquet',it)
    jLoopStop = time.time()
    print(jLoopStop-jLoopStart)
# dataFrame = pd.DataFrame(allGamesArray,columns=fields)
# table2 = pa.Table.from_pandas(allGamesArray)
# pq.write_table(table1, 'AllGameCombos.parquet')
#tempDominoList = list(allDominoIDs)

# Clean up stuff
del d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d0
end = time.time()
print(end-start)