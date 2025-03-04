import random

words = ["aardvark", "baboon", "camel"]

pickedWord = random.choice(words)
blankWord = "_" * len(pickedWord)
life = int(len(blankWord) * 1.5)
print(f"You have {life} life.")
while life > 0:
    inputChar = input(f"{blankWord} : ").lower()
    isRight = False
    blankCount = 0
    for i in range(0, len(blankWord)):
        if blankWord[i] == "_":
            blankCount += 1
            if pickedWord[i] == inputChar:
                blankWord = blankWord[:i] + inputChar + blankWord[i + 1:]
                isRight = True
    if blankCount == 1 and isRight: break
    if not isRight:
        life -= 1
        if life == 0: break
        print(f"Wrong, you have {life} life left")
if life == 0:
    print("Game over")
else:
    print(pickedWord+"\nYou won")
