import random

low = 1
high = 100
option = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.randint()
# option = random.choice(option)
random.shuffle(cards)

print(cards)