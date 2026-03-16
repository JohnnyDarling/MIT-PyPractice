
from random import randrange
from string import *
WORDLIST_FILENAME = "words.txt"

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = 'claptrap'
letters_guessed = []


# From part 3b:
def word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    word_result = False
    letters_result = []
    secret_word_length = len(secret_word)
    for i in secret_word:

        for j in letters_guessed:
            if i == j:
                letters_result.append(True)
                print(i)
#                print(letters_result)
    letters_result_length = len(letters_result)

    if letters_result_length == secret_word_length:
            word_result = True

    return word_result

    ####### YOUR CODE HERE ######
# print(word_guessed("claptrap", ['a','l','m','c','e','t','r','p','n']))
# print(word_guessed("claptrap", ['b','l','m','c','e','t','r','q','n']))"""

"""List1 = ['H', 'e', 'a', 'r']
string1 = ''
for i in List1:
    string1 = string1 + i
print(string1.lower())"""

def print_guessed(secret_word, letters_guessed):

    # global secret_word
    # global letters_guessed
    this_try = []
    this_try_string = ''
    ####### YOUR CODE HERE ######
    for i in secret_word:
        if i in letters_guessed:
            this_try.append(i)
        else:
            this_try.append('-')
    for j in this_try:
        this_try_string = this_try_string + j
    return this_try_string




# print(print_guessed("claptrap", ['a','l','m','c','e','t','r','p','n']))
# print(print_guessed("claptrap", ['b','l','m','c','e','t','r','q','n']))

test1 = print_guessed("claptrap", [])
assert test1 == '--------', 'test1 was ' + test1
test2 = print_guessed("claptrap", ['a','p'])
assert test2 == '--ap--ap', 'test2 was ' + test2
test3 = print_guessed("claptrap", ['a','l','m','c','e','t','r','p','n'])
assert test3 == 'claptrap', 'test3 was ' + test3

global secret_word
global letters_guessed
global mistakes_made
global MAX_GUESSES

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######

    # continually loop:
    while (mistakes_made < MAX_GUESSES):
        print(f"You have {MAX_GUESSES - mistakes_made} guesses left.")
        global secret_word
        global letters_guessed

        guess = input("Guess a letter: ").lower()[0]
        # Prints n guesses left
        for i in letters_guessed:
            if i == guess:
                print("You already guessed this letter.")
            else:
                letters_guessed.append(guess)

        print(print_guessed(secret_word, guess))
    #     check - has letter already been guessed?
    #         If so, what should I do?
    #         If not, what should I do?
    #     check - is letter in word?
    #         If so, what should I do?
    #         If not, what should I do?
        mistakes_made += 1

    return None
print(play_hangman())
