"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Adding a list of responces to incorrect guesses
try_again_responses_greater = ['Not quite, please try again. The number is greater than that.',
                               'So close, try again. Just a little higher.',
                               'Do not give up yet, keep going. Try something bigger',
                               'So sorry, keep trying. It is greater than that',
                               'Keep going you will get it soon. Guess a bigger number',]
try_again_responses_less = ['Not quite, please try again. The number is less than that.',
                               'So close, try again. Just a little lower.',
                               'Do not give up yet, keep going. Try something smaller',
                               'So sorry, keep trying. It is less than that',
                               'Keep going you will get it soon. Guess a smaller number',]
# Create the start_game function.
def start_game():
    # Write your code inside this function.
    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    #   2. Store a random number as the answer/solution.
    #   3. Continuously prompt the player for a guess.
    #     a. If the guess is greater than the solution, display to the player "It's lower".
    #     b. If the guess is less than the solution, display to the player "It's higher".

    #   4. Once the guess is correct, stop looping, inform the user they "Got it"
    #      and show how many attempts it took them to get the correct number.
    #   5. Let the player know the game is ending, or something that indicates the game is over.

    # ( You can add more features/enhancements if you'd like to. )
    name = input("What is your name?  ")
    print("|\n|")
    print("""Welcome, {}!!! This is the "Number Guessr" game.""".format(name))
    print("|\n|")
    while True:
        number = random.randrange(1, 11)
        value_error_response = '\nUh oh! It seems like you inputed an invalid answer, \nplease try again and put an integer for a number.'

        try:
            guess = int(input("Pick a number between 1-10.  "))
            attempts = 1
        except ValueError:
            print("{}".format(value_error_response))
        else:

        
            while guess != number:
                incorrect_responses_greater = random.choice(try_again_responses_greater)
                incorrect_responses_less = random.choice(try_again_responses_less)
                if number > guess:
                    try:
                        guess = int(input("\n{}  ".format(incorrect_responses_greater)))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                elif number < guess:
                    try:
                        guess = int(input("\n{}  ".format(incorrect_responses_less)))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                    
            
            if guess == number:
                print("\nCongradulations!!! You are a great guesser! The number is {}. \nIt took you {} attemps.".format(number, attempts))

                play_again = input("\n{}, would you like to play again? (Yes/No)  ".format(name))

                while True:
                    if play_again.lower() == 'yes':
                        break

                    elif play_again.lower() == 'no':
                        print("\nThank you for playing {}. See you next time!!!".format(name))
                        return
                        
                    else:
                        print("\nSorry, please answer with Yes/No")
                        play_again = input("\n{}, would you like to play again? (Yes/No)  ".format(name))
                  

# Kick off the program by calling the start_game function.
start_game()
