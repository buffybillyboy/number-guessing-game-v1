"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.

# Write your code inside this function.
def start_game():
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
    
    number = random.randrange(1, 11)
    
    guess = int(input("Pick a number between 1-10.  "))
    
    while guess != number:
        guess = int(input("Not quite, please try again.  "))
    
    while guess == number:
        print("Congradulations!!! You are a great guesser! The number is {}.".format(number))

        play_again = input("{}, would you like to play again? (Yes/No)  ".format(name))

        if play_again.lower() == 'yes':
            guess = int(input("Pick a number between 1-10.  "))
        elif play_again.lower() == 'no':
            print("Thank you for playing {}. See you next time!!!".format(name))
        else:
            print("Sorry, please answer with (Yes/No)")
            play_again = input("{}, would you like to play again? (Yes/No)  ".format(name))
                  

# Kick off the program by calling the start_game function.
start_game()
