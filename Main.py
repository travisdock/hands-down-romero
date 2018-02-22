import Setup
import Play
import random
import V1


discard = []
p1 = []
p2 = []
i = 'hello'
counter = 0

# Create Deck
deck = Setup.createshuffleddeck()
Setup.deal(p1, p2, deck)

# Turn card over
discard.insert(0, deck[0])
deck.remove(deck[0])

# who goes first
turn = random.randint(1, 2)

# Create players
name1 = V1.Pendejo(True, p1, discard, deck)
name2 = V1.Pendejo(True, p2, discard, deck)

# while loop to run through the game play
while counter != 3:
    if turn == 1:
        Play.turn(name1, p1, deck, discard)
        turn = 0
    else:
        Play.turn(name2, p2, deck, discard)
        turn = 1
    if counter == 0:
        break
    elif Play.knock() is False:
        counter = 0






