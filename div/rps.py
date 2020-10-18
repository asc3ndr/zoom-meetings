#!/usr/bin/python3
from random import choice, seed

# seed(15) # <--- Forces the computer to say 'Rock'

available_choices = {"rock": "paper", "paper": "scissor", "scissor": "rock"}
computer_choice = choice([key for key in available_choices.keys()])
user_choice = input("rock, paper, or scissor?\n").lower()

while user_choice not in available_choices.keys():
    user_choice = input("rock, paper, or scissor?\n").lower()

print(f"\nComputer says: {computer_choice}!\n")

if computer_choice == user_choice:
    print("It's a draw")
else:
    if user_choice in available_choices[computer_choice]:
        print("You win!")
    else:
        print("Computer wins!")
