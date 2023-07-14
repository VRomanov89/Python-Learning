import random
import math

#Warrior
class Warrior:
    def __init__(self, name = "Warrior", health = 0,attkMax = 0, blockMax = 0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + 0.5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)
        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    
    @staticmethod #capability of the class? - When you create a function that isn't related to the class - Ex: a Dog can't count!
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        print("{} attacks {} and dealt {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name,warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    maxomus = Warrior("Max", 50, 20, 10)
    galaxon = Warrior("Gal", 50, 20, 10)
    battle = Battle()
    battle.startFight(maxomus, galaxon)

main()