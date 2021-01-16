# http://www.codeskulptor.org/#user30_ScQBucGs2r_2.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
BALL_POS = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 20
BALL_VEL = [0.0,0.0]
PAD1_VEL = 0
PAD2_VEL = 0
KEY_DOWN = False
POS1 = 0
POS2 = 0
LEFT_COUNTER = 0
RIGHT_COUNTER = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global BALL_POS, BALL_VEL # these are vectors stored as lists
    BALL_POS = [WIDTH / 2, HEIGHT / 2]
    BALL_VEL = [0.0,0.0]
    if direction == False:
       BALL_VEL[0] = random.randrange(120, 240) / 60
       BALL_VEL[1] = random.randrange(60, 180) /60
       
        
    else:
       BALL_VEL[0] = -random.randrange(120, 240) / 60
       BALL_VEL[1] = -random.randrange(60, 180) /60
       
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global LEFT_COUNTER, RIGHT_COUNTER  # these are ints
    spawn_ball(RIGHT)
    LEFT_COUNTER = 0
    RIGHT_COUNTER = 0
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, BALL_POS, ball_vel,LEFT, RIGHT, KEY_DOWN
    global PAD_HEIGHT, PAD1_VEL, POS1, POS2, PAD2_VEL, LEFT_COUNTER, RIGHT_COUNTER
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]
    #collide and reflect off of left hand side of the canvas
    #Left side 
    if BALL_POS[0] <= BALL_RADIUS:
        
       if POS1 + PAD_HEIGHT >= BALL_POS[1] >= POS1:
            BALL_VEL[0] = -BALL_VEL[0] *1.1
       else:
                spawn_ball(LEFT)
                RIGHT_COUNTER += 1
                
    elif BALL_POS[1] <= BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1] * 1.1
        
    elif BALL_POS[0] >= 600-BALL_RADIUS:
       
        if POS2 +PAD_HEIGHT >= BALL_POS[1] >= POS2:
            BALL_VEL[0] = -BALL_VEL[0] *1.1
        else:
            spawn_ball(RIGHT)
            LEFT_COUNTER += 1
            
    elif BALL_POS[1] >= 400-BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]   *1.1
    
            
    # draw ball
    canvas.draw_circle(BALL_POS, BALL_RADIUS, 2, "white", "white")
    
    
   # update paddle's vertical position, keep paddle on the screen  
    
    
    POS1 = PAD1_VEL + POS1   
    POS2 = PAD2_VEL + POS2
    if POS1 >= 320:
        POS1 = 320
    if POS1 <= 0:
        POS1 = 0
    if POS2 >= 320:
        POS2 = 320
    if POS2 <= 0:
        POS2 = 0
    PAD1_POS = [(0, 0 + POS1), (0, PAD_HEIGHT + POS1)]
   
    PAD2_POS = [(600, POS2), (600, PAD_HEIGHT + POS2)]
    # draw paddles

    canvas.draw_line(PAD1_POS[0], PAD1_POS[1], 16, "white")
    canvas.draw_line(PAD2_POS[0], PAD2_POS[1], 16, "white")
    # draw scores
    canvas.draw_text(str(LEFT_COUNTER), (225, 30), 30, "white")
    canvas.draw_text(str(RIGHT_COUNTER), (375, 30), 30, "white")
def keydown(key):
    global PAD1_VEL, PAD1_POS, PAD_WIDTH, PAD_HEIGHT, KEY_DOWN, PAD2_VEL
    
    if key == simplegui.KEY_MAP['up']:
       PAD2_VEL = -5 
       
    elif key == simplegui.KEY_MAP['down']:
       PAD2_VEL = 5 
       
    elif key == simplegui.KEY_MAP['w']:
        PAD1_VEL = -5
        
    elif key == simplegui.KEY_MAP['s']:
        PAD1_VEL = 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel, PAD1_VEL, PAD2_VEL
    if key == simplegui.KEY_MAP['up']:
       PAD2_VEL = 0
       
    elif key == simplegui.KEY_MAP['down']:
       PAD2_VEL = 0
       
    elif key == simplegui.KEY_MAP['w']:
       PAD1_VEL = 0
        
    elif key == simplegui.KEY_MAP['s']:
       PAD1_VEL = 0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
