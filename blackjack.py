# http://www.codeskulptor.org/#user31_zzaKcyGSEx_0.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_hand = []
deadler_hand = []
deck = []
player_busted = False
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
outcome = ''
player_wins = 0
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
   
    def __init__(self):
        #initializes hand list and score variable
        self.hand = []
        self.score = 0
         
    def __str__(self):
        string_list = ''
        for x in self.hand:
            string_list = string_list + " " + str(x)
        return string_list
                
    def add_card(self, card):
        #appends Card to end of hand list.
        return self.hand.append(card)
               
    def get_value(self):
        self.score = 0
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace_in_hand = False   
        for x in self.hand:               
            if x.get_rank() == "A":
                ace_in_hand = True
            self.score = int(self.score) + int(VALUES[x.get_rank()])
     
        if ace_in_hand == True: #might need to add code
            if self.score < 12: #around here to facilitate 
                self.score += 10 #multiple aces or ace changes (11 to 1)
            else:
                pass                
        return self.score
    def draw(self, canvas, pos):
        count = 0   # draw a hand on the canvas, use the draw method for cards
        for c in self.hand:                        
            c.draw (canvas, (pos[0] + 100* count , pos[1]))
            count += 1 
           
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
       
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        self.counter = 0 
        for x in SUITS: #goes through SUIT
            for y in RANKS: #Pairs that SUIT with one of each RANK
                self.deck.append(Card(x,y)) #adds the created Object Card with SUIT AND RANK
                
        return random.shuffle(self.deck) #shuffles Deck
        
    def deal_card(self):        
        dealt_card = self.deck[0]        #card that is being dealt
        self.deck.pop(0) #deletes dealt_card from list
        return dealt_card #returns dealt_card
   
    def __str__(self):
        cards_in_deck = ''
        for x in self.deck:
            cards_in_deck = cards_in_deck + " " + str(x)
        return cards_in_deck
#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, outcome, player_busted, in_play, player_wins
    if in_play == True:
        player_wins -= 1
    # your code goes here
    in_play = True
    player_busted = False
    deck = Deck() #intiates object "deck" with Deck class
    deck.shuffle() #shuffles cards in deck
    player_hand = Hand() #iniates object "player hand" with Hand class
    dealer_hand = Hand() #iniiates object "dealer hand" '   ' 
    #adds the top four cards to the respective hands
    
    first_card = deck.deal_card()
    second_card = deck.deal_card()
    third_card = deck.deal_card()
    fourth_card = deck.deal_card()
    player_hand.add_card(first_card)
    player_hand.add_card(third_card)
    dealer_hand.add_card(second_card)
    dealer_hand.add_card(fourth_card)
    
    outcome = "Hit or Stand?" 
   
def hit():
    
    global player_hand, dealer_hand, deck, player_busted, outcome, in_play, player_wins
     # if the hand is in play, hit the player
    if player_busted == False and in_play == True:    
        card = deck.deal_card()   
        player_hand.add_card(card) 
        if player_hand.get_value() > 21:           
            player_busted = True 
            in_play = False
            player_wins -= 1
            outcome =  "Player busted! Deal again?"
        else: 
            pass
     
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer_hand, player_hand, deck, player_busted, outcome, in_play, player_wins
    player_score = player_hand.get_value()
    dealer_score = dealer_hand.get_value()
    in_play = False
    if player_busted == False:
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
   
        
        while dealer_score < 17:
            card = deck.deal_card()
            dealer_hand.add_card(card)
            dealer_score = dealer_hand.get_value()           
            
        if dealer_score > 21:
            player_wins += 1
            outcome = "Dealer Busts! You win! Deal again?"
        elif player_score > dealer_score:
            player_wins += 1
            outcome = "Player wins! New deal?"
        elif player_score <= dealer_score:
            player_wins -= 1
            outcome =  "Dealer wins! New deal?"
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    players_prompt = "Your score is: " + str(player_hand.get_value())
    dealers_prompt = "Dealer's score is: " + str(dealer_hand.get_value())
    player_score = "Player's score: " + str(player_wins)
    canvas.draw_text(players_prompt, (50, 475), 20, "black")
    canvas.draw_text(player_score, (300, 50), 30, "black")
    dealer_hand.draw(canvas, [50, 75])        
    player_hand.draw(canvas, [50, 350])
    canvas.draw_text(outcome, [50, 300], 30, "Black")
    canvas.draw_text("Blackjack!", [50 , 50], 30, "Black")
    if in_play == True:
        canvas.draw_line([50 + 35.5 , 26 + 49] , [50 + 35.5, 124 + 49], 80, "black")
        canvas.draw_line([50 + 35.5 , 26 + 55] , [50 + 35.5, 124 + 44], 74, "blue")
    else:
        canvas.draw_text(dealers_prompt, (50, 250), 20, "black") 
        # initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric