import os
import time
import math
from colorama import Fore,Style,Back,init

player1pos = [""]
player2pos = [""]

player1ships = ["carrier","battleship","destroyer","submarine","patrol boat"]
player2ships = ["carrier","battleship","destroyer","submarine","patrol boat"]

p1explodedtiles = []
p2explodedtiles = []

p1occupied= []
p2occupied= []


gameplayLoop = True

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


#############################################################################################
# THIS IS FOR PLAYER 1
# building board, placing ect
#############################################################################################

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

def checkp1shipcollide(elname,x,y):
    size = getSizeFromName(elname)
    for i in range(1, size):
        if f"{x+i},{y}" in p1occupied:
            print("this would be inside of another ship! try again!")
            return False
        if f"{x},{y+i}" in p1occupied:
            print("this would be inside of another ship! try again!")
            return False
        else:
            return True
        
def placeP1Ships():
    for i in player1ships:
        a=True
        while a == True:
            size = getSizeFromName(i)
            horizontal = i in ("carrier", "battleship")
            p1CurrentShipx = int(input(f"x position of {i}?"))-1
            if p1CurrentShipx > 8:
                print("please input a number between 1 and 8!")
                continue

            if horizontal and p1CurrentShipx + size > 8:
                print("invalid placement! try place more to the left")
                continue


            p1CurrentShipy = int(input(f"y position of {i}?"))-1
            if p1CurrentShipy > 8:
                print("please input a number between 1 and 8!")

            if (not horizontal) and p1CurrentShipy + size > 8:
                print("invalid placement! try place more upwards")
                continue
            if checkp1shipcollide(i,p1CurrentShipx,p1CurrentShipy):
                shipposition = f"{p1CurrentShipx},{p1CurrentShipy}"
                p1occupied.append(shipposition)
                print(p1occupied)
                print(player1ships)
                a=False
                placeextrap1(i,p1CurrentShipx,p1CurrentShipy)
                buildP1Board()
            else:
                continue
    
    
def buildP1Board():
    print(f"{Fore.GREEN}  1 2 3 4 5 6 7 8{Style.RESET_ALL}")
    for i in range(0,ymax):
        print(f"{Fore.GREEN}{i+1}{Style.RESET_ALL}",end=" ")
        for b in range(0,xmax):
            if f"{b},{i}" in p1explodedtiles and (f"{b},{i}" in p1occupied):
                print(f"{Back.RED}{Fore.BLACK}XX{Style.RESET_ALL}",end="")
            elif (f"{b},{i}" in p1explodedtiles):
                print(f"{Back.RED}{Fore.BLACK}~~{Style.RESET_ALL}",end="")
            elif f"{b},{i}" in p1occupied:
                print(f"{Back.CYAN}{Fore.BLACK}O {Style.RESET_ALL}",end="")
            else:
                print(f"{Back.CYAN}{Fore.CYAN}# {Style.RESET_ALL}",end="")
        print("")

def buildP1NOSHIPBoard():
    print(f"{Fore.GREEN}  1 2 3 4 5 6 7 8{Style.RESET_ALL}")
    for i in range(0,ymax):
        print(f"{Fore.GREEN}{i+1}{Style.RESET_ALL}",end=" ")
        for b in range(0,xmax):
            if (f"{b},{i}" in p1explodedtiles) and (f"{b},{i}" in p1occupied):
                print(f"{Back.RED}{Fore.BLACK}XX{Style.RESET_ALL}",end="")
            elif (f"{b},{i}" in p1explodedtiles):
                print(f"{Back.RED}{Fore.BLACK}~~{Style.RESET_ALL}",end="")
            else:
                print(f"{Back.CYAN}{Fore.CYAN}# {Style.RESET_ALL}",end="")
        print("")



#############################################################################################
# THIS IS FOR PLAYER 2
# building board, placing ect
#############################################################################################

def placeextrap2(elname,x,y):
    size = getSizeFromName(elname)


    if (elname == "carrier") or elname == ("battleship"):
        if x + size > 8:
                print("invalid placement! try place more to the left")

        for i in range(1, size):
            p2occupied.append(f"{i+x},{y}")

    if (elname == "submarine") or (elname == "patrol boat") or (elname == "destroyer"):
        for i in range(1, size):
            p2occupied.append(f"{x},{i+y}")

def checkp2shipcollide(elname,x,y):
    size = getSizeFromName(elname)
    for i in range(1, size):
        if f"{x+i},{y}" in p2occupied:
            print("this would be inside of another ship! try again!")
            return False
        if f"{x},{y+i}" in p2occupied:
            print("this would be inside of another ship! try again!")
            return False
        else:
            return True

def placeP2Ships():
    for i in player2ships:
        a=True
        while a == True:
            size = getSizeFromName(i)
            horizontal = i in ("carrier", "battleship")
            p2CurrentShipx = int(input(f"x position of {i}?"))-1
            if p2CurrentShipx > 8:
                print("please input a number between 1 and 8!")
                continue

            if horizontal and p2CurrentShipx + size > 8:
                print("invalid placement! try place more to the left")
                continue


            p2CurrentShipy = int(input(f"y position of {i}?"))-1
            if p2CurrentShipy > 8:
                print("please input a number between 1 and 8!")

            if (not horizontal) and p2CurrentShipy + size > 8:
                print("invalid placement! try place more upwards")
                continue
            if checkp2shipcollide(i,p2CurrentShipx,p2CurrentShipy):
                shipposition = f"{p2CurrentShipx},{p2CurrentShipy}"
                p2occupied.append(shipposition)
                print(p2occupied)
                print(player2ships)
                a=False
                placeextrap2(i,p2CurrentShipx,p2CurrentShipy)

                buildP2Board()
            else:
                continue
    
    
def buildP2Board():
    print(f"{Fore.GREEN}  1 2 3 4 5 6 7 8{Style.RESET_ALL}")
    for i in range(0,ymax):
        print(f"{Fore.GREEN}{i+1}{Style.RESET_ALL}",end=" ")
        for b in range(0,xmax):
            if (f"{b},{i}" in p2explodedtiles) and (f"{b},{i}" in p2occupied):
                print(f"{Back.RED}{Fore.BLACK}XX{Style.RESET_ALL}",end="")
            elif f"{b},{i}" in p2explodedtiles:
                print(f"{Back.RED}{Fore.BLACK}~~{Style.RESET_ALL}",end="")
            elif f"{b},{i}" in p2occupied:
                print(f"{Back.CYAN}{Fore.BLACK}O {Style.RESET_ALL}",end="")
            else:
                print(f"{Back.CYAN}{Fore.CYAN}# {Style.RESET_ALL}",end="")
        print("")

def buildP2NOSHIPBoard():
    print(f"{Fore.GREEN}  1 2 3 4 5 6 7 8{Style.RESET_ALL}")
    for i in range(0,ymax):
        print(f"{Fore.GREEN}{i+1}{Style.RESET_ALL}",end=" ")
        for b in range(0,xmax):
            if (f"{b},{i}" in p2explodedtiles) and (f"{b},{i}" in p2occupied):
                print(f"{Back.RED}{Fore.BLACK}XX{Style.RESET_ALL}",end="")
            elif f"{b},{i}" in p2explodedtiles:
                print(f"{Back.RED}{Fore.BLACK}~~{Style.RESET_ALL}",end="")
            else:
                print(f"{Back.CYAN}{Fore.CYAN}# {Style.RESET_ALL}",end="")
        print("")

#############################################################################################
# FIGHTING
# shooting and idk what else you would need
#############################################################################################

def shootAsP1():
    print("your board:\n\n")
    buildP1Board()
    print("\nP2'S BOARD")
    buildP2NOSHIPBoard()
    print("\n")
    print("where would you like to shoot on player 2's board?")
    p1shotx = int(input("x position\n> "))-1
    p1shoty = int(input("y position\n> "))-1
    currentshotcoords = f"{p1shotx},{p1shoty}"
    p2explodedtiles.append(currentshotcoords)
    if currentshotcoords in p2occupied:
        print(f"{Fore.GREEN}\nHIT! You hit a tile at {currentshotcoords}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}\nMISS! you missed a tile at {currentshotcoords}{Style.RESET_ALL}")

def shootAsP2():
    print("your board:\n\n")
    buildP2Board()
    print("\nP1'S BOARD")
    buildP1NOSHIPBoard()
    print("\n")
    print("where would you like to shoot on player 1's board?")
    p2shotx = int(input("x position\n> "))-1
    p2shoty = int(input("y position\n> "))-1
    currentshotcoords = f"{p2shotx},{p2shoty}"
    p1explodedtiles.append(currentshotcoords)
    if currentshotcoords in p1occupied:
        print(f"{Fore.GREEN}\nHIT! You hit a tile at {currentshotcoords}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}\nMISS! you missed a tile at {currentshotcoords}{Style.RESET_ALL}")

def checkifwon():
    checkingp1ships = p1occupied
    for i in p1explodedtiles:
        try:
            checkingp1ships.remove(i)
        except ValueError:
            pass
    if checkingp1ships == []:
        print("PLAYER 2 WINS!")
        gameplayLoop = False
        exit()

    checkingp2ships = p2occupied
    for i in p2explodedtiles:
        try:
            checkingp2ships.remove(i)
        except ValueError:
            pass
    if checkingp2ships == []:
        print("PLAYER 2 WINS!")
        gameplayLoop = False
        exit()
#gameplay start

displayrules()
placeP1Ships()
clear()
buildP1Board()
input("\n\n\n press enter and give to player 2. ")
clear()
displayrules()
placeP2Ships()
clear()
buildP2Board()
input("\n\n\n press enter and give to player 1 to begin! ")


while gameplayLoop:
    shootAsP1()
    checkifwon()
    input("\ngive to player 2 and press enter! ")
    shootAsP2()
    checkifwon()
    input("\ngive to player 1 and press enter! ")