import os
import time
import math

player1pos = [""]
player2pos = [""]

player1ships = ["carrier","battleship","destroyer","submarine","patrol boat"]
player2ships = ["carrier","battleship","destroyer","submarine","patrol boat"]

player1shipsplaced = []
player1shipsplaced = []

p1occupied= []
p2occupied= []

xmax = 8 
ymax = 8

def displayrules():
    print("RULES\n" +
    "both players get an 8x8 grid to place their ships\n" +
    "carrier: 5 units right\n" +
    "battleship: 4 units right\n" +
    "destroyer/submarine: 3 units down\n" +
    "patrol boat: 2 units down\n\n" +
    "you have to guess where the other player's ships are and shoot them in turns\n" +
    "good luck\n\n"          
    )

    input("press enter if you understand!\n")

def clear():
    os.system("cls||clear")


def getSizeFromName(ship):
    if ship == "carrier":
        size = 5
    elif ship == "battleship":
        size = 4
    elif ship == "destroyer":
        size = 3
    elif ship == "submarine":
        size = 3
    elif ship == "patrol boat":
        size = 2
    return size
        
def placeextrap1(elname,x,y):
    size = getSizeFromName(elname)


    if (elname == "carrier") or elname == ("battleship"):
        if x + size > 8:
                print("invalid placement! try place more to the left")

        for i in range(1, size):
            p1occupied.append(f"{i+x},{y}")

    if (elname == "submarine") or (elname == "patrol boat") or (elname == "destroyer"):
        for i in range(1, size):
            p1occupied.append(f"{x},{i+y}")


        
def placeP1Ships():
    for i in player1ships:
        a=True
        while a == True:
            size = getSizeFromName(i)
            p1CurrentShipx = int(input(f"x position of {i}?"))-1
            if p1CurrentShipx > 8:
                print("please input a number between 1 and 8!")
                continue

            if p1CurrentShipx + size > 8:
                print("invalid placement! try place more to the left")
                continue


            p1CurrentShipy = int(input(f"y position of {i}?"))-1
            if p1CurrentShipy > 8:
                print("please input a number between 1 and 8!")

            if p1CurrentShipy + size > 8:
                print("invalid placement! try place more upwards")
                continue
            shipposition = f"{p1CurrentShipx},{p1CurrentShipy}"
            p1occupied.append(shipposition)
            print(p1occupied)
            print(player1ships)
            a=False
            placeextrap1(i,p1CurrentShipx,p1CurrentShipy)


            buildP1Board()
    
    
def buildP1Board():
    print("  1 2 3 4 5 6 7 8")
    for i in range(0,ymax):
        print(i+1,end=" ")
        for b in range(0,xmax):
            if f"{b},{i}" in p1occupied:
                print("O ",end="")
            else:
                print("# ",end="")
        print("")


displayrules()
placeP1Ships()
clear()
buildP1Board()
