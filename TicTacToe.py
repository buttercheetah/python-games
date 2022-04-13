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
def printboard():
    print("Board")
def check_mark(row, col):
    print("check if exists")
def place_mark(row, col):
    print("placing")
def checkifwin(id):
    print("checking")
