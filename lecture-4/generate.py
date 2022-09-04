

from random import choice, randint, shuffle


def main():
    cards = ["jack", "queen", "king"]
    
    shuffle(cards)
    
    for card in cards:
        print(card)
    
main()