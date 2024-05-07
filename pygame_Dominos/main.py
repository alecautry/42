from functions import *
import csv
from itertools import *

d1 = DOMINO(0,0,0,True) 
d2 = DOMINO(1,1,0,False)
d3 = DOMINO(2,1,1,True)
d4 = DOMINO(3,2,0,False)
d5 = DOMINO(4,2,1,False)
d6 = DOMINO(5,2,2,True)
d7 = DOMINO(6,3,0,False)
d8 = DOMINO(7,3,1,False)
d9 = DOMINO(8,3,2,False)
d10 = DOMINO(9,3,3,True)
d11 = DOMINO(10,4,0,False)
d12 = DOMINO(11,4,1,False)
d13 = DOMINO(12,4,2,False)
d14 = DOMINO(13,4,3,False)
d15 = DOMINO(14,4,4,True)
d16 = DOMINO(15,5,0,False)
d17 = DOMINO(16,5,1,False)
d18 = DOMINO(17,5,2,False)
d19 = DOMINO(18,5,3,False)
d20 = DOMINO(19,5,4,False)
d21 = DOMINO(20,5,5,True)
d22 = DOMINO(21,6,0,False)
d23 = DOMINO(22,6,1,False)
d24 = DOMINO(23,6,2,False)
d25 = DOMINO(24,6,3,False)
d26 = DOMINO(25,6,4,False)
d27 = DOMINO(26,6,5,False)
d28 = DOMINO(27,6,6,True)

z = range(28)
y = range(27)
x = range(26)
w = range(25)
v = range(7)

allDominos = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28]
trump = 3
setTrump(allDominos, trump)

combo = list(permutations(z, 4))
chainCombo = chain.from_iterable(permutations(z, 4))
print("Chain")

print("Combo")
print(combo)
with open('trickWinner.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["trump","Dlead.ID", "d2.ID", "d3.ID", "d4.ID", "winner"]
    writer.writerow(field)
    for e in v:
        trump = e
        setTrump(allDominos, trump)
        for a in z:
            for b in y:
                for c in x:
                    for d in w:
                        winner = trickWinner2(allDominos[a], allDominos[b], allDominos[c], allDominos[d])
                        saveString = [trump, allDominos[a].ID, allDominos[b].ID, allDominos[c].ID, allDominos[d].ID, winner]
                        writer.writerow(saveString)



winner = trickWinner2(d7,d24,d13,d9) # 3/0, 6/2, 4/2, 3/2
print(winner) # 4
winner = trickWinner2(d7,d9,d10,d28) # 3/0, 3/2, 3/3, 6/6
print(winner) # 3
#TODO Create a for loop to test each combination of dominos and save to a file

# Clean up stuff
del d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28