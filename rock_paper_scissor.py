#This Is A Dice Game Created By Kishor S

from random import randint

#Create a list of play options
t = ("rock", "paper", "scissor")
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
    #set player to true
    player = input("\n\nrock, paper, scissor:\n>>> ")
    print(">>> " + computer)
    if player == computer:
        print("TIE")
    elif player == "rock":
        if computer == "scissor":
            print("You Win")
        else:
            print("You Loose")
    elif player == "paper":
        if computer == "rock":
            print("You Win")
        else:
            print("You Loose")
    elif player == "scissor":
        if computer == "paper":
            print("You Win")
        else:
            print('You Loose')
    else:
        print("I Don't Understand That")
    #Player was set to True so we set it to True so the loop continues
    player = False
    computer = t[randint(0,2)]   

