choice1 = input ('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    #Continue in the game
    choice2 = input("You've come to the late, type 'wait to wait for a boat, or 'swim' to swim across.").lower()
    if choice2 == "wait":
        #continue
        choice3 = input("You arrive at an island. Three houses - red, yellow, blue. Chich color do you choose?").lower()
        if choice3 == "red":
            print("Room of fire! GG")
        elif choice3 == "yellow":
            print("You win!")
        elif choice3 == "blue":
            print("Beasts! GG")
        else:
            print("Game over! Wrong door")
    else:
        print("Angry trout!")
else:    
    print("Game Over.")
