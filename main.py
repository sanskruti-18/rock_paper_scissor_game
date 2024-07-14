'''
-1 for rock
1 for paper
0 for scissors
'''
import random

youDict = {"r": -1, "p": 1, "s": 0}
revDict = {-1 : "rock", 1: "paper", 0: "sccissors"} 

while True:
    computer = random.choice([1,0,-1])

    print("MENU\nr for rock\np for paper\ns for sccissors")
    youstr = input("Enter your choice: ")

    if youstr not in youDict:
        print("Invalid choice\nPlease try again")
        continue

    you = youDict[youstr]

    print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")

    if(computer == you):
        print("It's a Draw!")

    else:
        if(computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1): 
            print("You win!")

        elif(computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
            print("You Lose!") 

        else:
            print("Something went wrong!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower() # strip()
    if play_again != 'yes':
        print("Thanks for playing!")
        break