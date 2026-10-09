import keyboard
import os

x = 0
y = 0
selected = "1,1"
xowns = []
oowns = []
gameison = True
currentplayer = 1

winningcombos = [
    ["0,0","1,0","2,0"], ["0,1","1,1","2,1"], ["0,2","1,2","2,2"],
    ["0,0","0,1","0,2"], ["1,0","1,1","1,2"], ["2,0","2,1","2,2"],
    ["0,0","1,1","2,2"], ["2,0","1,1","0,2"]
]

def buildBoard():
    global currentplayer
    os.system("cls||clear")
    for b in range(0,3):
        for a in range(0,3):
            if f"{a},{b}" == selected:
                if f"{a},{b}" in xowns:
                    print("(X)",end=" ")
                elif f"{a},{b}" in oowns:
                    print("(O)",end=" ")
                else:
                    print("( )",end=" ")
            else:
                if f"{a},{b}" in xowns:
                    print("[X]",end=" ")
                elif f"{a},{b}" in oowns:
                    print("[O]",end=" ")
                else:
                    print("[ ]",end=" ")
        print("\n")
    if currentplayer == 1:
        print("X's turn!")
    elif currentplayer == 2:
        print("O's turn!")

def clear():
    os.system("cls||clear")

def up():
    global x,y,selected
    if y > 0:
        y -= 1
    selected = f"{x},{y}"
    buildBoard()

def down():
    global x,y,selected
    if y < 2:
        y += 1
    selected = f"{x},{y}"
    buildBoard()

def left():
    global x,y,selected
    if x > 0:
        x -= 1
    selected = f"{x},{y}"
    buildBoard()

def right():
    global x,y,selected
    if x < 2:
        x += 1
    selected = f"{x},{y}"
    buildBoard()

def place():
    global currentplayer,xowns,selected
    if currentplayer == 1:
        xowns.append(selected)
        currentplayer = 2
    elif currentplayer == 2:
            oowns.append(selected)
            currentplayer = 1
    buildBoard()
    checkforwin()


def checkforwin():
    global gameison
    for line in winningcombos:
        if all(cell in xowns for cell in line):
            print("X wins!")
            gameison = False
            quit()
        if all(cell in oowns for cell in line):
            print("O wins!")
            gameison = False
            quit()
    if len(xowns) + len(oowns) == 9:
        print("Draw!")
        gameison = False
        quit()


keyboard.add_hotkey("up", up)
keyboard.add_hotkey("down", down)
keyboard.add_hotkey("left", left)
keyboard.add_hotkey("right", right)
keyboard.add_hotkey("space", place)


keyboard.wait("esc")



buildBoard()