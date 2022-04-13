import time
import random
import os
import platform
osv = platform.system()
def clearscreen(): #a simple function to clear the screen so the game board looks nice
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
def printboard(): #simply prins out the board surrounded by a box
    print("  A B C")
    print(" ┌─────┐")
    print("1│" + ralps(l1) + "│")
    print("2│" + ralps(l2) + "│")
    print("3│" + ralps(l3) + "│")
    print(" └─────┘")
def check_mark(row, col): #checks if the position is taken
    if row == 1:
        if l1[col] == "*": return False
        else: return True
    elif row == 2:
        if l2[col] == "*": return False
        else: return True
    elif row == 3:
        if l3[col] == "*": return False
        else: return True
def place_mark(row, col, id): #places a move
    if check_mark(row, col): return False
    else:
        if row == 1: l1[col] = id
        elif row == 2: l2[col] = id
        elif row == 3: l3[col] = id
        return True
def winnermessage(player, lostplayer):
    ms = random.randrange(1,15)
    if ms == 1: print('Congratulations and BRAVO on your win ' + str(player) + "!")
    elif ms == 2: print("This calls for celebrating! Congrats " + str(player) + "!")
    elif ms == 3: print("I knew it was only a matter of time. Well done " + str(player) + "!")
    elif ms == 4: print("You've worked so hard for this. Congrats " + str(player) + "!")
    elif ms == 5: print("I've got a feeling this is only the beginning of even more great things to come for you!\n" + str(player) + " Wins!")
    elif ms == 6: print("You were born to win, but to be a winner, you must plan to win, prepare to win, and expect to win. - Zig Ziglar\ni guess you took that to heart " + str(player))
    elif ms == 7: print("Winners don't wait for chances, they take them! Well done " + str(player) + "!")
    elif ms == 8: print("Sometimes you lose... but not this time! Good job " + str(player) + "!")
    elif ms == 9:
        print(str(lostplayer) + ": I am inevitable")
        time.sleep(2)
        print(str(player) + ": and I am Ironman")
        time.sleep(2)
        print("Valiant win " + str(player))
    elif ms == 10: 
        print("Congrats " + str(lostplayer), end="")
        time.sleep(2)
        print(" on LOOSING")
        print(str(player)+ " Wins!")
    elif ms == 11: 
        print("The world is filled with heroes and wannabes",end="")
        for i in range(5):
            time.sleep(0.5)
            print(".",end="")
        print(" Good thing your the real deal " + str(player))
    elif ms == 12: print("if only " + str(lostplayer) + " could rewind time.\n" + str(player) + " wins!")
    elif ms == 13:
        print("Unkown: Did you ever hear the tragedy of " + lostplayer + "?")
        time.sleep(2)
        print(str(player) + ": No.")
        time.sleep(0.5)
        print("Unkown: I thought not. It's not a story the Jedi would tell you. It's a Sith legend.")
        time.sleep(2)
        print("Unkown: " + lostplayer + "... was a Dark Lord of the Sith so powerful and so wise, he could use the Board to influence the midi-chlorians... to create... life. ")
        time.sleep(4)
        print("Unkown: He had such a knowledge of the dark side, he could even keep the ones he cared about... from dying.")
        time.sleep(2)
        print(str(player) + ": He could actually... save people from death?")
        time.sleep(2)
        print("Unkown: The dark side of the Board is a pathway to many abilities... some consider to be unnatural.")
        time.sleep(3)
        print(str(player) + ": What happened to him?")
        time.sleep(2)
        print("Unkown: He became so powerful, the only thing he was afraid of was... losing his power. Which eventually, of course, he did.")
        time.sleep(4)
        print("Unkown: Unfortunately, he taught his apprentice everything he knew. Then his apprentice killed him in his sleep. It's ironic. He could save others from death, but not himself.")
        time.sleep(4)
        print(str(player) + ": Is it possible to learn this power?")
        time.sleep(2)
        print("Unkown: Not from a looser.")
        time.sleep(1.5)
        print(str(player) + " Wins!")

    else:
        print(str(player) + " wins!")
def checkifwin(): #checks if a player has won and then prints out who won
    if l1[0] == l1[1] and l1[1] == l1[2] and l1[2] != "*":
        if l1[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l2[0] == l2[1] and l2[1] == l2[2] and l2[2] != "*":
        if l2[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l3[0] == l3[1] and l3[1] == l3[2] and l3[2] != "*":
        if l3[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l1[0] == l2[1] and l3[2] == l1[0] and l1[0] != "*":
        if l1[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l3[0] == l2[1] and l1[2] == l3[0] and l3[0] != "*":
        if l3[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l1[0] == l2[0] and l3[0] == l1[0] and l1[0] != "*":
        if l1[0] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l1[1] == l2[1] and l3[1] == l1[1] and l1[1] != "*":
        if l1[1] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    elif l1[2] == l2[2] and l3[2] == l1[2] and l1[2] != "*":
        if l1[2] == "X":
            winnermessage("X", "0")
        else:
            winnermessage("0", "X")
        return True
    else:
        return False
print("Will there be multiple players?\ny/N") #optional AI
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
        if mp: #checks if there are two players playing, if so it displays whos turn it is
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
                    print("Movement outside possible range!")
                    print(0 + "") #purposefully breaking try so it doesnt reach bottom
                if int(choce[1]) > 3 or choce[1] == 0:
                    print("Movement outside possible range!")
                    print(0 + "") #purposefully breaking try so it doesnt reach bottom
                if mp:
                    if Player1play:
                        idp = "0"
                    else:
                        idp = 'X'
                else:
                    idp = 'X'
                thing = place_mark(int(choce[1]), colum, idp)
                if thing == False:
                    print("Piece already there!")
                    print(0 + "") #purposefully breaking try so it doesnt reach bottom
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
        time.sleep(1)
        if Player1play and Player2play:
            break
    if gameover == False and mp == False:
        otherplay = place_mark(random.randrange(1,4), random.randrange(0,3), "0")
        while otherplay == False:
            otherplay = place_mark(random.randrange(1,4), random.randrange(0,3), "0")
        Player2play = True
