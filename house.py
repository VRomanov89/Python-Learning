name = input("What is your name? ")

match name:
    case "Harry":
        print("Gryff")
    case "Herm":
        print("Graff")
    case _:
        print("Who?")