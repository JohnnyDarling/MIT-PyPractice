# Name: Brendan Lautissier
# Section:
# nims.py

def play_nims(pile, max_stones):

    valid_choice = range(1, max_stones + 1)
    new_pile = pile

    while new_pile > 0:
        player_1 = 0
        player_2 = 0
        while player_1 not in valid_choice:
            player_1 = int(input("P1, how many stones do you take?: "))
            if player_1 in valid_choice:
                new_pile -= player_1
                print(new_pile)
                if new_pile <= 0:
                    print("Player 1 wins!")
                    return "GAME OVER"
            else:
                print("Invalid choice, please try again")

        while player_2 not in valid_choice:
            player_2 = int(input("P2, how many stones do you take?: "))
            if player_2 in valid_choice:
                new_pile -= player_2
                print(new_pile)
                if new_pile <= 0:
                    print("Player 2 wins!")
                    return "GAME OVER"
            else:
                print("Invalid choice, please try again")

print(play_nims(100, 5))



'''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#print(play_nims(100, 5))
#print("Game over")