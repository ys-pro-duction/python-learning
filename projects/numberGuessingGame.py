import random


def play():
    attempt = int(input("How many attempt you need: "))
    numberTo = int(input("Number range from 0 to : "))
    numberToGuess = random.randint(1, numberTo)
    while attempt > 0:
        guess = int(input(f"Guess number({attempt} left): "))
        if guess == numberToGuess:
            print("You won!!")
            return
        elif guess > numberToGuess:
            print(f"{guess} is higher number")
        else:
            print(f"{guess} is lower number")
        attempt -= 1
    print("You loose")


play()
while input("Play one more game [Y/n]: ").lower() == "y":
    play()
