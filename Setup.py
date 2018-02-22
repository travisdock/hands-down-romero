import random

discard = []
p1 = []
p2 = []


# Create two decks that are shuffled and return the shuffled deck
def createshuffleddeck():
    deck = [i + 1 for i in range(104)]
    random.shuffle(deck)
    return deck


# Deal 7 cards to each player from the top of the deck (index[0] being the top of the deck
def deal(player1, player2, dex):
    for a in range(7):
        player1.insert(a, dex[a])
        player2.insert(a, dex[a+7])
        dex.remove(dex[a])
        dex.remove(dex[a+7])


