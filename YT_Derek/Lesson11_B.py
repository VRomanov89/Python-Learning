class Dog:
    num_of_dogs = 0
    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1
    
    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spt")
    doug = Dog("Doug")
    spot.getNumOfDogs()

main()