# http://www.codeskulptor.org/#user30_ScQBucGs2r_2.py

# template for "Stopwatch: The Game"

import simplegui

# define global variables

display = "0:00.0"
counter = 0
milliseconds = 0
seconds = 0
ten_seconds = 0
minutes = 0
games_attempted = 0
games_won = 0
games_displayed = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global display, milliseconds, seconds, ten_seconds, minutes
      
    if t % 600 == 0:
        minutes += 1
        ten_seconds = 0
        seconds = 0
        milliseconds = 0
    elif t % 100 == 0:
        ten_seconds += 1
        seconds = 0
        milliseconds = 0
    elif t % 10 == 0:
        seconds += 1
        milliseconds = 0   
    else:
        milliseconds += 1
               
    display = str(minutes) + ":" + str(ten_seconds) + str(seconds) + "." + str(milliseconds)     
    
# define event andlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
def Stop():    
    
    global milliseconds, games_attempted, games_won, games_displayed
    if timer.is_running() == True:
        if milliseconds == 0:
            games_attempted += 1
            games_won += 1
            games_displayed = str(games_won) + "/" + str(games_attempted)
        else:
            games_attempted += 1
            games_displayed = str(games_won) + "/" + str(games_attempted)        
        timer.stop()
    else:
        pass
    
def Reset():
    
    global counter, display, milliseconds, seconds, ten_seconds, minutes, games_displayed, games_attempted, games_won
    timer.stop()
    counter = 0
    milliseconds = 0
    seconds = 0
    ten_seconds = 0
    minutes = 0
    display = "0:00.0"
    games_displayed = "0/0"
    games_attempted = 0
    games_won = 0
    
    
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    
    global counter  
    counter += 1
    format(counter)
    
# define draw handler

def draw_handler(canvas):
    
    canvas.draw_text(display, (100,150), 75, "Red")  
    canvas.draw_text(games_displayed, (260,20), 20, "red")
    
# create frame

frame = simplegui.create_frame("Let's Play Stopwatch!", 300, 200)

#buttons

start_button = frame.add_button("Start", Start, 100)
stop_button = frame.add_button("Stop", Stop, 100)
reset_button = frame.add_button("Reset", Reset, 100)

#Canvas

frame.set_draw_handler(draw_handler)

#Timer

timer = simplegui.create_timer(100, time_handler)

# register event handlers


# start frame

frame.start()
# Please remember to review the grading rubric
