import random
import statistics

coin = random.choice(["heads", "tails"])
print(coin)

num = random.randint(1,10)
print(num)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

print(statistics.mean([100,90]))