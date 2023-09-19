from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too High!")
    elif guess < answer:
        print("Too low!")
    else:
        print(f"Corret - {answer}")


def set_difficulty():
    level = input("Choose a difficulty - 'easy' or 'hard'? ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print ("WElcome to the game!")
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining!")

    answer = randint(1, 100)
    print(f"The answer is {answer}")

    guess = 0
    while answer != guess or turns > 0:
        guess = int(input("Make a guess! "))
        check_answer(guess, answer)

game()