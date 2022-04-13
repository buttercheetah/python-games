import time
import random
import os
import platform
osv = platform.system()
def clearscreen():
    if (osv == "Windows"):
        os.system('cls')
    elif (osv == "Linux"):
        os.system('clear')
    elif (osv == "Darwin"):
        os.system('clear')
l1 = ['*','*','*']
l2 = ['*','*','*']
l3 = ['*','*','*']
def ralps(string): #remove annoying list print stuff
    return str(string).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
def printboard():
    print("  A B C")
    print(" ┌─────┐")
    print("1│" + ralps(l1) + "│")
    print("2│" + ralps(l2) + "│")
    print("3│" + ralps(l3) + "│")
    print(" └─────┘")
def check_mark(row, col):
    if row == 1:
        if l1[col] == "*":
            return False
        else:
            return True
    elif row == 2:
        if l2[col] == "*":
            return False
        else:
            return True
    elif row == 3:
        if l3[col] == "*":
            return False
        else:
            return True
def place_mark(row, col, id):
    if check_mark(row, col):
        return False
    else:
        if row == 1:
            l1[col] = id
        elif row == 2:
            l2[col] = id
        elif row == 3:
            l3[col] = id
        return True
def checkifwin():
    if l1[0] == l1[1] and l1[1] == l1[2] and l1[2] != "*":
        print('Player ' + l1[1] + ' won!')
        return True
    elif l2[0] == l2[1] and l2[1] == l2[2] and l2[2] != "*":
        print('Player ' + l2[1] + ' won!')
        return True
    elif l3[0] == l3[1] and l3[1] == l3[2] and l3[2] != "*":
        print('Player ' + l3[1] + ' won!')
        return True
    elif l1[0] == l2[1] and l3[2] == l1[0] and l1[0] != "*":
        print('Player ' + l3[2] + ' won!')
        return True
    elif l3[0] == l2[1] and l1[2] == l3[0] and l3[0] != "*":
        print('Player ' + l1[2] + ' won!')
        return True
    elif l1[0] == l2[0] and l3[0] == l1[0] and l1[0] != "*":
        print('Player ' + l3[0] + ' won!')
        return True
    elif l1[1] == l2[1] and l3[1] == l1[1] and l1[1] != "*":
        print('Player ' + l3[1] + ' won!')
        return True
    elif l1[2] == l2[2] and l3[2] == l1[2] and l1[2] != "*":
        print('Player ' + l3[2] + ' won!')
        return True
    else:
        return False
print("Will there be multiple players?\ny/N")
mp = input()
if mp.lower() == "y":
    mp = True
else:
    mp = False
gameover = False
while True:
    if gameover:
        break
    Player1play = False
    Player2play = False
    while True:
        clearscreen()
        print("Welcome", end="")
        if mp:
            if Player1play:
                print(" player 2")
            else:
                print(" player 1")
        printboard()
        gameover = checkifwin()
        if gameover:
            break
        print("Please input placement or type EXIT to quit\nExample: A1")
        choce = input()
        if choce == 'EXIT':
            gameover = True
            break
        elif len(choce) > 2:
            print("too long")
        elif len(choce) < 2:
            print("Too short")
        else:
            try:
                if choce[0].lower() == "a": colum = 0
                elif choce[0].lower() == "b": colum = 1
                elif choce[0].lower() == "c": colum = 2
                else:
                    print(0 + "") #purposefully breaking try so it doesnt reach bottom
                if int(choce[1]) > 3 or choce[1] == 0:
                    print(0 + "") #purposefully breaking try so it doesnt reach bottom
                if mp:
                    if Player1play:
                        idp = "0"
                    else:
                        idp = 'X'
                else:
                    idp = 'X'
                place_mark(int(choce[1]), colum, idp)
                if mp:
                    if Player1play:
                        Player2play = True
                    else:
                        Player1play = True
                else:
                    Player1play = True
                    break
            except:
                pass
        if Player1play and Player2play:
            break
    if gameover == False and mp == False:
        otherplay = place_mark(random.randrange(1,4), random.randrange(0,3), "0")
        while otherplay == False:
            otherplay = place_mark(random.randrange(1,4), random.randrange(0,3), "0")
        Player2play = True
