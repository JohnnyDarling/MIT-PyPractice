# Brendan Lautissier
# Rock, Paper, Scissors

Player_1 = input("Player 1 Rock, Paper or Scissors: ").lower()
Player_2 = input("Player 2 Rock, Paper or Scissors: ").lower()
options = ['rock', 'paper', 'scissors']

if Player_1 not in options or Player_2 not in options:
    print("You are Error!")

elif Player_1 == Player_2:
    print("Draw!")
elif (Player_1 == "rock" and Player_2 == "scissors") or \
    (Player_1 == "paper" and Player_2 == "rock") or \
    (Player_1 == "scissors" and Player_2 == "paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")