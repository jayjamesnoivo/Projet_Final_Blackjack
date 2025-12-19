import random

def creer_paquet():
    valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    couleurs = ["♠", "♥", "♦", "♣"]
    paquet = []
    for v in valeurs:
        for c in couleurs:
            paquet.append(f"{v}{c}")
    random.shuffle(paquet)
    return paquet

def distribuer_carte(paquet):
    return paquet.pop()
