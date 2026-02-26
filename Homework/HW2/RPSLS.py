# Rock, Paper, Scissors, Lizard, Spock

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# and Rock crushes Scissors.

import random

def rpsls(user_choice):
    options = ["rock", "paper", "scissors", "lizard", "spock"]

# Catch-All Invalid Input
    if user_choice not in options:
        return "You are Error!"

    computer_choice = random.choice(options)
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

# Catch-All Draws
    if user_choice == computer_choice:
        return "Draw"
# All of the 'Win' Conditions
    elif user_choice == "rock"      and computer_choice == "scissors"   or \
         user_choice == "rock"      and computer_choice == "lizard"     or \
         user_choice == "paper"     and computer_choice == "rock"       or \
         user_choice == "paper"     and computer_choice == "spock"      or \
         user_choice == "scissors"  and computer_choice == "paper"      or \
         user_choice == "scissors"  and computer_choice == "lizard"     or \
         user_choice == "lizard"    and computer_choice == "paper"      or \
         user_choice == "lizard"    and computer_choice == "spock"      or \
         user_choice == "spock"     and computer_choice == "rock"       or \
         user_choice == "spock"     and computer_choice == "scissors":
        return "You win!"
# If you didn't win nor tie, then it's a loss
    else:
        return "You lose!"

print (rpsls(user_choice = input("Choose Rock, Paper, Scissors, Lizard, Spock: ").lower()))