import random
from math import trunc

rock = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

scissor = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

moves = [rock,paper,scissor]
while True:
    user = int(input("User input(rock=0, paper=1, scissor=2): "))
    print(moves[user])
    computer = int(random.randint(0,2))
    print(f"computer input: {computer}\n{moves[computer]}")
    if user == computer:
        print("Game draw!!")
    elif user == 0 and computer == 1:
        print("Computer win!!")
    elif user == 0 and computer == 2:
        print("User win!!")
    elif user == 1 and computer == 0:
        print("User win!!")
    elif user == 1 and computer == 2:
        print("Computer win!!")
    elif user == 2 and computer == 0:
        print("Computer win!!")
    elif user == 2 and computer == 1:
        print("User win!!")

