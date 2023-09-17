import random

#Words for the game
word_list = ["ardvark", "baboon", "camel"]

#Randomly choose one word
chosen_word = random.choice(word_list)

#User will input a letter
guess = input("Guess a letter:").lower()

#Check word against letter
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")