# Snake Water Gun Game
import random
choices = ["s","w","g"]
comp_choice = random.choice(choices)
u_choice = input("ENTTER:[s] for snake [w] for water [g] for gun \n").lower()
if(u_choice not in choices):
    while(u_choice not in choices):
        print("Wrong selection")
        u_choice = input("ENTTER:[s] for snake [w] for water [g] for gun \n").lower()
print(f"==> Machine choose {comp_choice}")
print(f"==> Player choose {u_choice}")
if(u_choice==comp_choice):
    print("Draw")
elif(u_choice=="w"):
    if(comp_choice=="s"):
        print("Machine Wins!, Try Again")
    elif(comp_choice=="g"):
        print("You Wins!, Congrats")
elif(u_choice=="s"):
    if(comp_choice=="w"):
        print("You Wins!, Congrats")
    elif(comp_choice=="g"):
        print("Machine Wins!, Try Again")
elif(u_choice=="g"):
    if(comp_choice=="w"):
        print("Machine Wins!, Try Again")
    elif(comp_choice=="s"):
        print("You Wins!, Congrats")