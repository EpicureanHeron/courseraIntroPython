# http://www.codeskulptor.org/#user29_aN3nwlqXjW_9.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code

secret_number = random.randint(0, 100)

number_of_guesses = 7

counter = 1

# helper function to start and restart the game
def new_game():
    global secret_number, counter
    counter = 1
    print "Alright, let's play 'guess the number!'" 
    if number_of_guesses == 7:
        print "Guess within the range 0 - 100"
        print  "You have 7 chances to win!"
        secret_number = random.randint(0, 100)
    elif number_of_guesses == 10:
        print "Guess within the range 0 - 1000" 
        print "You have 10 chances to win"
        secret_number = random.randint(0 , 1000)
    
# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number, counter, number_of_guesses
    number_of_guesses = 7
    counter = 0
    new_game()
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number, counter, number_of_guesses
    
    number_of_guesses = 10
    counter = 0
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    global secret_number, counter, number_of_guesses
    guess = int(guess)
    turns_remaining = number_of_guesses - counter
    if turns_remaining > 0:
        print "You guessed", guess
        if guess > secret_number:
            counter += 1
            print "Try guessing lower"
            print "Turns remaining:", turns_remaining
        elif guess < secret_number:
            counter += 1
            print "Try guessing higher"
            print "Turns remaining:", turns_remaining
        elif guess == secret_number:
            print  "You win!"
            new_game()
    else:
        print "You guessed", guess 
        print "Sorry, why don't you try again?" 
        new_game() 
# create frame
new_game()

f = simplegui.create_frame("Guess the Number", 200, 200)

inp = f.add_input("Enter Your Guess Below!", input_guess, 100)
button1 = f.add_button("Range 0 - 100", range100)
button1 = f.add_button("Range 0 - 1000", range1000)
