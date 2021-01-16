# http://www.codeskulptor.org/#user29_iZ09AlcCpR_40.py

import random

def name_to_number(name):
    
    if name == "rock":
        name_number = 0
        return name_number
    elif name == "Spock":
        name_number = 1
        return name_number
    elif name == "paper":
        name_number = 2
        return name_number 
    elif name == "lizard":
        name_number = 3
        return name_number 
    elif name == "scissors":
        name_number = 4
        return name_number
    else:
        return "Error in name_to_number"

def number_to_name(number):
    if number == 0:
        number_name = "rock"
        return number_name
    elif number == 1:
        number_name = "Spock"
        return number_name
    elif number == 2:
        number_name = "paper"
        return number_name
    elif number == 3:
        number_name = "lizard"
        return number_name
    elif number == 4:
        number_name = "scissors"
        return number_name
    else:
        print "Error in number_to_name"

def rpsls(player_choice): 
    print " "
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(4)
    comp_choice = number_to_name(int(comp_number))
    
    print "Player choses", player_choice
    print "Computer choses", comp_choice
    
    difference = (player_number - comp_number) 
    modulo = difference % 5
    
    if modulo == 0:
        print "Player and computer tie!"
    elif modulo == 1:
        print "Player wins!"
    elif modulo == 2:
        print "Player wins!"
    elif modulo == 3:
        print "Computer wins!"
    elif modulo == 4:
        print "Computer wins!"
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")