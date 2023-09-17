import random

user_choice = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number!")
elif user_choice == 0 and computer_choice == 2:
    print ("You win!")
elif computer_choice > user_choice:
    print ("You lose")
elif user_choice > computer_choice:
    print ("You win!")
elif computer_choice == user_choice:
    print("Draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
