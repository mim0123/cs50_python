# Study the python documentation for random
# Use of import

import random

coin = random.choice(["heads", "tails"])
print(coin)


# Use of from 

from random import choice

coin = choice(["heads", "tails"])
print(coin)


# Use of random.randint

import random 

number = random.randint(1,10)
print(number)


# Use of random.shuffle


import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)