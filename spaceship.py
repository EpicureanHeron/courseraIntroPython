# http://www.codeskulptor.org/#user33_3H7YvaKO7i_36.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_35.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_34.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_33.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_32.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_31.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_30.py
# http://www.codeskulptor.org/#user33_3H7YvaKO7i_24.py
# http://www.codeskulptor.org/#user32_3H7YvaKO7i_16.py

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
rock_group = set([])
missile_group = set([])
started = True

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
thrust_info = ImageInfo([135, 45], [90, 90], 35)
thrust_image = ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.spin = False
        self.angle = angle
        self.angle_vel = 0
        self.accel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        
        if self.thrust == False:
            canvas.draw_image(ship_image, ship_info.get_center(), ship_info.get_size(), self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(thrust_image, thrust_info.get_center(), thrust_info.get_size(), self.pos, self.image_size, self.angle)
    def update(self):
        # updates velocity times acceleration
        if self.thrust == True:                          
            self.accel += .005
            
            #checks the angle of the ship, sets vel according to provided function
            forward_vector = angle_to_vector(self.angle)
            
            self.vel[0] += (forward_vector[0] * self.accel) *.50
            self.vel[1] += (forward_vector[1] * self.accel) *.50
        
        else:
            self.accel = 0
            self.vel[0] *= .99
            self.vel[1] *= .99
       
        # updates angle with angle_vel
        self.angle += self.angle_vel
        #updates position based on velocity
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos = [self.pos[0]%800, self.pos[1]%600]
    def inc_angle(self, key):        
        
        if self.spin == True:
            if key == "right":
                #sets angle_vel to increment angle to the right
                self.angle_vel = .08
                #sets angle_vel to increment angle to the left
            elif key == "left":
                self.angle_vel = -.08
        else:
            self.angle_vel = 0
            
            
    def shoot(self):
        global missile_group
        # calculates the forward vector based on current angle of ship
        forward_vector_missile = angle_to_vector(self.angle)
       
        # sets velocity for missile
        missile_vel = [forward_vector_missile[0] * 5, forward_vector_missile[1] * 5]
        # adds velocity of ship to velocity of missile
        missile_vel = [missile_vel[0] + self.vel[0] , missile_vel[1] + self.vel[1]]
        # calculates the tip of the ship based on radius of ship and forward vector
        ship_tip = [self.pos[0] + (self.radius*forward_vector_missile[0]), self.pos[1] + (self.radius*forward_vector_missile[1])]                
        # creates object from Sprite class with the given variable above
        # adds object to the global missile_group 
        missile_group.add(Sprite(ship_tip, missile_vel, self.angle, self.angle_vel, missile_image, missile_info, missile_sound))
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size , self.angle)
    
    def update(self):
       
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos =  [self.pos[0] % 800, self.pos[1] % 600]
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
            
    def collide(self, other_object):
         # compares radii to distance of center points
         # if the distance is less than the combined radii, returns True or False
        if self.radius + other_object.radius > dist(self.pos, other_object.pos):
            return True
        else:
            return False
# Key Handlers
    
def key_down(key):
    
    # key down for "up" key, changes thrust to True and plays thrust sound
    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = True
               
        ship_thrust_sound.play()
    # key down for "right" key, changes spin to True and calls the inc_angle handler in ship Class    
    if key == simplegui.KEY_MAP['right']:
        my_ship.spin = True
        my_ship.inc_angle("right")
    # key down for "left" key, changes spin to True and calls the inc_angle handler in ship Class    
    if key == simplegui.KEY_MAP['left']:
        my_ship.spin = True
        my_ship.inc_angle("left")
    # key down for "space" key, calls the shoot() handler in Ship class  
    if key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
     
def key_up(key):
                  
    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = False
        
        ship_thrust_sound.rewind()
        
    elif key == simplegui.KEY_MAP['right']:
        my_ship.spin = False
        my_ship.inc_angle("right")
       
    elif key == simplegui.KEY_MAP['left']:
        my_ship.spin = False
        my_ship.inc_angle("left")

def process_sprite_group(group, canvas):
# calls each object in set and calls its draw function on the canvas
# updates  
    removal_set = set([])
    for i in group:
        i.update
        if i.update() == True:
            removal_set.add(i)
        else:                    
            i.draw(canvas)
            
           
    group.difference_update(removal_set)
def group_collide(group, other_object):
    # takes a group (must be a sprite or have collide method    # 
    # checks if the Sprite class' method returns True
    # if it does, adds the set object to the removal list and subtracts life    
    # after cycle, compares removal_list to the group
    # then updates "group" by taking out everything in removal_set     
    
    removal_set = set([])
    for i in group:
        
        if i.collide(other_object) == True:
            removal_set.add(i)
    group.difference_update(removal_set)       
        
    if len(removal_set) > 0:
        return True
    else:
        return False                          

def group_group_collide(group_1, group_2):
    global score
    group_group_copy = group_1.copy()
    group_group1_removal = set([])
    
    for instance in group_group_copy:
        if group_collide(group_2, instance) == True:
            score += 1
            group_group1_removal.add(instance)
    
    group_1.difference_update(group_group1_removal)    

def new_game():
    global started, lives, score
    started = True
    timer.start()
    lives = 3
    score = 0
        
def mouse_handler(position):
    global started
    if started == False:
        new_game()
    else:
        pass

    
        
def draw(canvas):
    global time, lives, started, missile_group, rock_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Lives: " + str(lives), (25,50), 50, "green")
    
    canvas.draw_text("Score: " + str(score), (600, 50), 50, "green")
    # draw ship and sprites
    if lives <= 0:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        started = False
        
    if started == False:
        timer.stop()
        missile_group = set([])
        rock_group = set([])
        soundtrack.rewind()
    else:
        soundtrack.play()
    my_ship.draw(canvas)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    
    # update ship and sprites
    my_ship.update()
    if group_collide(rock_group, my_ship) == True:
        lives -= 1
        
       
    
    group_group_collide(rock_group, missile_group)
     

# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, score
    random_vel = [random.randrange(-1, 1), random.randrange(-4, 4)]
    multiplier = score // 10
    random_vel[0]*multiplier
    random_vel[1]*multiplier
    random_pos = [random.randrange(0, 800), random.randrange(0 , 600)]
    random_angle_vel = random.randrange(-2, 2)
    random_angle_vel *= .1
    if len(rock_group) < 12:
        if dist(random_pos, my_ship.pos) > my_ship.radius + 30:        
            rock_group.add(Sprite(random_pos, random_vel, 0, random_angle_vel, asteroid_image, asteroid_info))
       
    else:
        pass
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)


# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_mouseclick_handler(mouse_handler)

# get things rolling
timer.start()
frame.start()
