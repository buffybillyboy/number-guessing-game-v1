"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import random
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
# start_game function
def start_game():

    high_score = 0
    
    # Asking the user their name
    name = input("What is your name?  ")
    # Printing out a welcome
    print("|\n|")
    print("""Welcome, {}!!! This is the "Number Guessr" game.""".format(name))
    print("|\n|")


    # Creating a loop so you can replay the game
    while True:
        # Creating some variables to use in the loop
        number = random.randrange(1, 11)
        value_error_response = '\nUh oh! It seems like you inputed an invalid answer, \nplease try again and put an integer for a number.'

        # Prompting user to guess a number while taking care of bugs
        try:
            guess = int(input("Pick a number between 1-10.  "))
            attempts = 1
        except ValueError:
            print("{}".format(value_error_response))
        else:


            # A loop that deals with the user guessing a wrong number
            while guess != number:
                # Adding some variables that randomize the output of the incorrect responses list for better user experience
                incorrect_responses_greater = random.choice(try_again_responses_greater)
                incorrect_responses_less = random.choice(try_again_responses_less)
                out_of_range = 'Sorry, your guess is out of the range of this game. \nPlease guess a number between 1-10.'
            
                # Adding feedback to the user if their guess is out of range
                if guess > 10:
                    print("{}".format(out_of_range))
                    try:
                        guess = int(input("Pick a number between 1-10.  "))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                elif guess < 1:
                    print("{}".format(out_of_range))
                    try:
                        guess = int(input("Pick a number between 1-10.  "))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                # This if statement deals with if the users guess is greater than the number genereated and prevents bugs
                elif number > guess:
                    try:
                        guess = int(input("\n{}  ".format(incorrect_responses_greater)))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                # This elif statement deals with if the users guess is less than the number genereated and prevents bugs
                elif number < guess:
                    try:
                        guess = int(input("\n{}  ".format(incorrect_responses_less)))
                        attempts += 1
                    except ValueError:
                        print("{}".format(value_error_response))
                    
            # This if statement deals with when you user guesses correctly
            if guess == number:
                if high_score == 0:
                    high_score = attempts
                elif high_score > attempts:
                    high_score = attempts
                    print("\nYay! You have a new high score! It is {}.".format(high_score))
                print("\nCongratulations!!! You are a great guesser! The number is {}. \nIt took you {} attemps. Your high score is {}.".format(number, attempts, high_score))
                # This variable asks the user if they would like to play again
                play_again = input("\n{}, would you like to play again? (Yes/No)  ".format(name))
                # This while loop prevents bugs from happening based on the users response
                while True:
                    # This if statement deals with if the user wants to play again
                    if play_again.lower() == 'yes':
                        break
                    # This elif statement deals with if the user does not want to play agian
                    elif play_again.lower() == 'no':
                        print("\nThank you for playing {}. See you next time!!!".format(name))
                        return
                    # This else statement deals with if the user does not say 'yes' or 'no' when prompted if they want to play again   
                    else:
                        print("\nSorry, please answer with Yes/No")
                        play_again = input("\n{}, would you like to play again? (Yes/No)  ".format(name))
                  

# Calls start_game function
start_game()
