# Draw a card from the top of the deck and put it in players hand. Remove card from deck
def drawone(player, dex):
    player.append(dex[0])
    dex.remove(dex[0])


def pickupdiscard(player, discards):
    player.append(discards[0])
    discards.remove(discards[0])


# Remove card from hand and add it to the discard pile.
def discard(player, discards, index):
    player.remove(player[index])
    discards.insert(0, player[index])


def knock():
    return True


def showhand(player):
    newlist = [i + 1 for i in range(len(player))]

    for i in range(0, len(player)):
        number = player[i] % 13
        if number == 0:
            number += 13
        if player[i] in range(0, 26):
            newlist[i] = str(number) + " of hearts"
        elif player[i] in range(26, 52):
            newlist[i] = str(number) + " of diamonds"
        elif player[i] in range(52, 78):
            newlist[i] = str(number) + " of clubs"
        else:
            newlist[i] = str(number) + " of spades"
    for j in range(len(player)):
        print("Position", j, ": ", newlist[j])


def turn(player, hand, deck, discards):
    x = ""
    print(player, "'s Turn:\n")
    print("Your action choices are: \n"
          "Press '1' to pick up a card \n"
          "Press '2' to pick up the discard \n"
          "press '3' to discard \n"
          "press'4' to knock \n"
          "press '5' to finish your turn \n")

    while x != '5':
        x = player()
        if x == '1':
            drawone(hand, deck)
        elif x == '2':
            pickupdiscard(hand, discards)
        else:
            print("that is not a valid action")

    while x != '5':
        x = player()
        if x == '3':
            discard(hand, discards)
        else:
            print("that is not a valid action")

