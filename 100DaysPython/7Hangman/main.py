import random

#Words for the game
word_list = ["ardvark", "baboon", "camel"]

#Randomly choose one word
chosen_word = random.choice(word_list)

#
display = []
for letter in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    #User will input a letter
    guess = input("Guess a letter:").lower()

    #Check word against letter
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")