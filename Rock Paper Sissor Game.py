#Rock Paper Scissors game
import random
l=["rock","scissor","paper"]
while True: 
    usercount=0
    compcount=0 
    userchoice=int(input('''
Game Start.....
1 Yes
2 No | Exit '''))
    if userchoice==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock
2 Scissor
3 Paper'''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            compchoice=random.choice(l)
            if compchoice==uchoice:
                print("Computer Value",compchoice)
                print("User Value",uchoice)
                print("Game Draw")
                usercount=usercount+1
                compcount=compcount+1
            elif(uchoice=="rock" and compchoice=="scissor") or (uchoice=="paper" and compchoice=="rock") or (uchoice=="scissor" and compchoice=="paper"):
                print("Computer Value",compchoice)
                print("User Value",uchoice)
                print("You Won..!!!")
                usercount=usercount+1
            else:
                print("Computer Value",compchoice)
                print("User Value",uchoice)
                print("You Lose Computer Won..!!!")
                compcount=compcount+1

                      




    else:
        break