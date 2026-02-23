# Import necessary modules
import pygame as py
import os
import sys

# Initialize Pygame
py.init()

# Set the camera offset
camera_offset_x = 0

# Set the resolution of the game window
resolution_width = 1280
resolution_height = 720  # Running 720p currently
win = py.display.set_mode((resolution_width, resolution_height))

# Player spawn position
player_x_position = 50
player_y_position = 469.5
player_position = [player_x_position, player_y_position]

#Platform Zones
platform_zones = [900]
on_ground = True
in_collision = False
falling_through_platform = False

# Player Size
width = 25
length = 50

# Player Velocity (AKA Speed)
vel = 10
run_vel = 15

# Accumulator variables
jump = False
jc = 12
active = True
player_facing_right = True


# Function to draw a block and handle player positions
def block(posx, posy, width, height, r, g, b, x):
    # Draw a rectangle on the window with given parameters
    py.draw.rect(win, (r, g, b), (posx, posy, width, height))
    if player_x_position == 'x':  # This condition seems incorrect; likely should be `x`
        return player_x_position
    else:
        return player_y_position


# Set the window title
py.display.set_caption('Super Goombario')


# Player class definition
class Player(py.sprite.Sprite):
    # Initialize the player
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.images = []
        self.img = py.image.load(os.path.join('Mario V1.png')).convert_alpha()
        self.img = py.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_image(self, player_facing_right):
        if not player_facing_right:
            self.image = py.transform.flip(self.images[0], True, False)
        else:
            self.image = self.images[0]


# Tile class definition
class tile(py.sprite.Sprite):
    # Initialize a tile
    def __init__(self, x, y, img):
        py.sprite.Sprite.__init__(self)
        self.block = py.image.load(os.path.join(img)).convert_alpha()
        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.block


# Set up grass tiles and their positions
grass_locations = []
grass_list = py.sprite.Group()
tile_s = 32
for i in range(150):
    grass_locations.append(tile_s * i)
for i in range(len(grass_locations)):
    grass_holder = tile(grass_locations[i], 560, 'Ground V1.png')
    for w in range(0, 160, 32):
        dirt_holder = tile(grass_locations[i], 560 + w, 'Ground V1.png')
        grass_list.add(dirt_holder)
    grass_list.add(grass_holder)


# Function to create a platform at a given offset
def platform1(offset,offset_y,size):
    p1l = []
    platsg = py.sprite.Group()
    for i in range(size):
        p1l.append(tile_s * i + 900 + offset)
    for i in range(len(p1l)):
        platholder = tile(p1l[i], offset_y, 'Ground V1.png')
        platsg.add(platholder)
    return platsg

platform1_group = platform1(camera_offset_x, 400, 10)
player = Player()
player.rect.x = 500
player.rect.y = 450
player_list = py.sprite.Group()
player_list.add(player)

# --Runs player's movements--
while active:
    py.time.delay(25)
    for event in py.event.get():
        if event.type == py.QUIT:
            active = False

    # print(1000 + camera_offset_x, "LESS")
    # print(1000 + 200 + camera_offset_x, "MORE")
    # print(player_x_position)








        # player.img = py.transform.flip(player.img, True, False)

        # --Gets what key the player has pressed--
    key = py.key.get_pressed()

    # else:
    # camera_offset_x = 0
    player.rect.x = player_x_position
    player.rect.y = player_y_position


    #if player_x_position >= (855 + camera_offset_x) and player_x_position <= (1210 + camera_offset_x) and player_y_position <= 432 and jump == True and on_ground == True:
        #print("Moved")
        #player_y_position = 310
        #jump = False
        #on_ground = False
       # jc = 12

    #elif on_ground == False and jump == False and not player_x_position >= (855 + camera_offset_x) or not player_x_position <= (1210 + camera_offset_x):

        #if not player_y_position == 469.5:
           # player_y_position += 15.95
            #player_y_position = round(player_y_position,2)
            #print(player_y_position)
      #  else:
           # on_ground = True
           # player_y_position == 469.5









    if not player_x_position >= 630 and key[py.K_d] or key[py.K_RIGHT] and player_x_position >= 630:
        player_x_position += vel
        if player_facing_right == False:
            player_facing_right = True
            player.update_image(player_facing_right)
    else:
        player_x_position == 630

    # --Key D--
    if player_x_position == 630 and key[py.K_d] or key[py.K_RIGHT] and player_x_position == 630:
        print("D")

        if player_facing_right == False:
            player_facing_right = True
            player.update_image(player_facing_right)

        if key[py.K_d] and key[py.K_LSHIFT] or key[py.K_RIGHT] and key[py.K_LSHIFT]:
            camera_offset_x += -(run_vel)

        else:
            camera_offset_x += -(vel)

    # --Key A--
    if player_x_position == 615 and key[py.K_a] or key[py.K_LEFT] and player_x_position == 615:
        print("A")

        if player_facing_right == True:
            player_facing_right = False
            player.update_image(player_facing_right)

        if key[py.K_a] and key[py.K_LSHIFT] or key[py.K_LEFT] and key[py.K_LSHIFT]:
            camera_offset_x += run_vel

        else:
            camera_offset_x += vel

    elif key[py.K_a] or key[py.K_LEFT]:

        if player_facing_right == True:
            player_facing_right = False
            player.update_image(player_facing_right)

        if key[py.K_a] and key[py.K_LSHIFT] or key[py.K_LEFT] and key[py.K_LSHIFT]:
            camera_offset_x += run_vel

        else:
            camera_offset_x += vel

    # --Key S-- (But first determines if player is mid-air/jumping)
    if key[py.K_s] and player_y_position < 469.5 or key[py.K_DOWN] and player_y_position < 469.5:
         falling_through_platform = True


    if falling_through_platform:
        if player_y_position < 469.5:
            player_y_position += 32
        else:
            player_y_position = 469.5
            falling_through_platform = False



    if jump == False:

        # --Key W-- (But first determines if player is mid-air/jumping)
        if key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]:
            jump = True


    # --Deals with the player jumping
    else:
        if jc >= -12:
            player_y_position -= (jc * abs(jc)) * (1 / 3)
            jc -= 1


        else:  # This will execute if our jump is finished
            jc = 12
            jump = False

    collision_list = py.sprite.spritecollide(player, platform1_group, False)

    # Create a sprite group for Platform1
    platform1_group = platform1(camera_offset_x, 400, 10)

    # Inside the main game loop after the player's position update
    # Check for collisions between the player and Platform1
    collision_list = py.sprite.spritecollide(player, platform1_group, False)

    if not falling_through_platform:  # Check if falling through platform is not activated
        if collision_list:
            for platform in collision_list:
                if player_y_position < platform.rect.centery:  # Adjust if player is above the platform
                    player_y_position = platform.rect.top - player.rect.height
                    on_ground = False  # Set on_ground to False when colliding with a platform
                    jump = True  # Disable jumping
                    in_collision = True
                else:
                    player_y_position = platform.rect.bottom  # Adjust player Y position to platform top


    # Check if the player has reached the floor (ground)
    if player_y_position >= 469.5:
        player_y_position = 469.5  # Set player's Y position to the floor level
        on_ground = True  # Consider the player on the ground




    # Redraw the player at the new position
    player.rect.x = player_x_position
    player.rect.y = player_y_position
    player_list.draw(win)

    # Redraw the player at the new position
    player.rect.x = player_x_position
    player.rect.y = player_y_position

    # camera_offset_x = resolution_width // 2 - player_x_position - width // 2

    win.fill((173, 216, 230))  # Fills the screen with blue

    # player =  py.draw.rect(win, (76, 12, 200),  (player_x_position, player_y_position, width, length))  # This takes: window/surface, color, rect

    # py.draw.rect(win, (200, 76, 12), (0, 560, 10000, 800))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    # py.draw.rect(win, (200, 76, 12),
    # (camera_offset_x, 590, 10000, 500))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    block((50 + camera_offset_x), 50, 100, 100, 0, 0, 0, player_x_position)  # THIS IS THE BLACK BOX


    player_list.draw(win)

    grass_list.draw(win)
    # py.draw.rect(win, (255, 255, 255), player.rect, 2)
    platform1(camera_offset_x,400,10).draw(win)

    block((1210 + camera_offset_x), 432, 10, 10, 0, 0, 0, player_x_position)

    py.display.update()

    # --Prints player cord's, currently commeted out, cause reduces frames
    # print(player_x_position, ',', player_y_position)
py.quit()