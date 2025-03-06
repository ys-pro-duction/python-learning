import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardWithVal = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
               'K': 10, }
while True:
    userCards = []
    copCards = []
    userCards.append(random.choice(cards))
    userCards.append(random.choice(cards))
    copCards.append(random.choice(cards))
    copCards.append(random.choice(cards))
    userCardSum = cardWithVal[userCards[0]] + cardWithVal[userCards[1]]
    copCardSum = cardWithVal[copCards[0]]
    print("====Cards=====")
    print(f"User cards: {userCards} = {userCardSum}")
    print(f"Computer cards: [{copCards[0]}, ?] = {copCardSum}")
    moreCards = input("Do you want 1 more card: [Y/n] ").lower()
    if moreCards == "y":
        userCards.append(random.choice(cards))
        userCardSum += cardWithVal[userCards[2]]
    copCardSum += cardWithVal[copCards[1]]

    for card in userCards:
        if userCardSum > 21 and card == 'A':
            userCardSum -= 10
    for card in copCards:
        if copCardSum > 21 and card == 'A':
            copCardSum -= 10
    print("======Card Revel======")
    print(f"User cards: {userCards} = {userCardSum}")
    print(f"Computer cards: {copCards} = {copCardSum}")
    if userCardSum == copCardSum:
        print("Game draw")
    elif userCardSum > 21:
        print("Game over\nUser loose")
    elif userCardSum < copCardSum:
        print("Game over\nUser loose")
    else: print("User Win!!")

    playMore = input("Play more [Y/n]: ").lower()
    if playMore != "y": break
