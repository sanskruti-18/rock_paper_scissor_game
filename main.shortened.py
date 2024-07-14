'''
-1 for rock
1 for paper
0 for scissors
'''
import random
computer = random.choice([1,0,-1])

youDict = {"r": -1, "p": 1, "s": 0}
revDict = {-1 : "rock", 1: "paper", 0: "sccissors"} 

youstr = input("MENU\nr for rock\np for paper\ns for sccissors\nEnter your choice: ")
you = youDict[youstr]

print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")

if(computer == you):
    print("It's a Draw!")

if((computer - you) == -1 or  (computer - you) == 2 ):
    print("You lose!")
else:
    print("You win!") 

'''    

else:
    if(computer == -1 and you == 1):  # comp - you = -2
        print("You win!")

    elif(computer == -1 and you == 0):  # -1
        print("You lose!")

    elif(computer == 1 and you == 0):  # 1
        print("You win!")

    elif(computer == 1 and you == -1):  # 2
        print("You lose!")

    elif(computer == 0 and you == 1):  # -1
        print("You lose!")

    elif(computer == 0 and you == -1):  # 1
        print("You win!")

    else:
        print("Something went wrong!")
        
'''