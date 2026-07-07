#STONE,PAPER,SCISSOR

# rock-case:

# r-r=tie
# r-p=p win
# r-s- r win

# paper-case:

# p-p=tie
# p-r=p win
# p-s=s win


# sicssor-case:

# s-s=tie
# s-r=r win
# s-p=s win


#start the program
import random

print("====WELCOME TO THE GAME====")

#Display the choices
list_choice=["stone","paper" ,"scissor"]
print(list_choice)
while True:

#Ask user to choose option

    user_move=input("Enter your move: ").lower()

    #generate the computer choice randomly
    computer_move=random.choice(list_choice)

    if user_move not in list_choice:
        print("Invalid Move! Please choose stone, paper, or scissor.")
        continue

    #compare user_choice with computer_choice
    print(f"user_choice= {user_move}, computer_choice= {computer_move}")

    #both choices are the same, the result is Draw
    if (user_move == computer_move):
         print("both choose same so the Match is : Draw")
    elif user_move=="stone":
        if computer_move=="paper":
            print(" paper cover stone: computer win")
        else:
            print("stone smashed scissor: you win")
    elif user_move=="paper":
        if computer_move=="stone":
            print("paper cover stone: you win")
        else:
            print("scissor cut the paper: computer win")
    elif user_move=="scissor":
        if computer_move=="paper":
            print("scissor cut the paper: you win")
        else:
            print("stone smashed scissor: computer win")
#ask your if you want to play again if yes repaet the game 
    play_again = input("Do you want to play again? (yes/no): ").lower()
    #if no end the program
    if play_again == "no":
        print("Thanks for playing!")
        break
            


