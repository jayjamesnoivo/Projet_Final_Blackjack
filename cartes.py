import random

def create_deck():
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #10 = face card & 11 = ace
    deck = []
    for v in values:

       deck.append(v)
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    return deck.pop()
