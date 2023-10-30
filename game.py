#ROCK PAPER SCISSORS GAME

import random

op={0:"Rock",1:"Paper",2:"Scissors"}

def compute_winner(ip1,ip2):
    if ip1==0:
        if ip2==0:
            return 0
        if ip2==1:
            return 2
        if ip2==2:
            return 1
    elif ip1==1:
        if ip2==0:
            return 1
        if ip2==1:
            return 0
        if ip2==2:
            return 2
    else:
        if ip2==0:
            return 2
        if ip2==1:
            return 1
        if ip2==2:
            return 0

pscore=0
cscore=0
flag=True

while(flag):
    print("Enter 0 for rock,1 for paper and 2 for scissors")
    ip1=int(input())
    if ip1 in op:
        print(f"You chose {op[ip1]}")
        ip2=random.randint(0,2)
        print(f"Computer chose {op[ip2]}")
        winner=compute_winner(ip1,ip2)
        if winner==1:
            pscore+=1
            print(f"You won...Your score is {pscore}\nComputer's score is {cscore}")
        elif winner==0:
            print(f"It's a draw...\nYour score is {pscore}\nComputer's score is {cscore} ")
        else:
            cscore+=1
            print(f"Computer won...\nYour score is {pscore}\nComputer's score is {cscore}")
        flag=int(input("Enter 1 to continue 0 to quit: "))
        if flag!=1:
            flag=0
        
    else:
        print("Enter a valid number")
