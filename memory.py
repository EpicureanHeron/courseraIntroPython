# http://www.codeskulptor.org/#user31_IwJ8VYHAa5yHCI8_3.py

# implementation of card game - Memory

import simplegui
import random

cards = []
cards_2 = []

cards = range(0, 8)
cards_2= range(0, 8)

cards.extend(cards_2)

exposed = {}
counter = 0


ordered_deck = {}
state = 0
turns = "Turn = 0"
card_1 = 0
last_card = 0
index1 = 0
last_index = 0
correct_matches = {}

# helper function to initialize globals
def new_game():
    global cards, exposed, state, correct_matches, turns, card_1, last_card, index1, last_index
    global turns, counter
    random.shuffle(cards) 
    for x in range(16):
        exposed[x] = False
    for x in range(16):
        ordered_deck[x] = cards[x]
    for x in range(16):
        correct_matches[x] = False
    state = 0
    turns = 0
    card_1 = 0
    last_card = 0
    index1 = 0
    last_index = 0
    counter = 0
    turns = "Turns = 0"
    label.set_text(turns)   
        
         
# define event handlers
def mouseclick(pos):
    global state, card_1, last_card, index1, last_index, correct_matches, counter, turns
    if state == 0:
        if exposed[pos[0] // 50] == False:
            index1 = pos[0] // 50 
            card_1 = ordered_deck[pos[0] // 50]
            exposed[pos[0] // 50] = True
            state = 1
            counter += 1
            turns = "Turns = " + str(counter)
            label.set_text(turns)
    elif state == 1:
        if exposed[pos[0] // 50] == False:
            last_card = card_1
            last_index = index1
            index1 = pos[0] // 50
            exposed[pos[0] // 50] = True
            card_1 = ordered_deck[pos[0] // 50]
            state = 2 
            
    else:
        if last_card == card_1:
            correct_matches[last_index] = True
            correct_matches[index1] = True
        
        if exposed[pos[0] // 50] == False:
            counter += 1
            turns = "Turns = " + str(counter)
            label.set_text(turns)
            card_1 = ordered_deck[pos[0] // 50]  
            index1 = pos[0] // 50
            for x in range(16):
                if exposed[x] == True:
                    exposed[x] = False
                    state = 1
                    
        exposed[pos[0] // 50] = True              
            
      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, ordered_deck, correct_matches
    move = 15
    divider = 0
    
    for x in range(16):
        
        canvas.draw_line((0 + divider, 0), (0 + divider, 100), 2 , "red")
        #Draws Card Face Up
        if correct_matches[x] == True:
            
            canvas.draw_text(str(ordered_deck[x]), [move, 60], 30, "blue")
            move += 50
            divider += 50
        elif exposed[x] == True:       
            
            canvas.draw_text(str(ordered_deck[x]), [move, 60], 30, "blue")

            move += 50
            divider += 50
            
        #Obscures Card    
        else:
            canvas.draw_line((25 + divider, 0), (25 + divider, 100), 50, "green")
            divider += 50
            move  += 50
            
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label(turns)

label.set_text(turns)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric