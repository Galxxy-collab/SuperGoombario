#Import necessary modules
import pygame as py
import os
import sys

#https://code-with-me.global.jetbrains.com/ZMbp8Rn85_2s0dowIs_doA#p=PC&fp=1E99570F43DC2D4ECEAAD5CF6A800A7A264CA58EE43E7A707405663FF1C95287
#Initialize Pygame
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
ground_height  = 469.5
player_position = [player_x_position, player_y_position]

# Player Size
width = 25
length = 50

# Player Velocity (AKA Speed)
vel = 10
run_vel = 15
# Accumulator variables
# set variables needed for jumping
jump = [False]
jc = 12
jc2 = 12
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
        # get images needed for player
        self.images = []
        self.img = py.image.load(os.path.join('../Images/supergoomba.png')).convert_alpha()
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
    def player_x(self):
        return self.rect.x
    def player_y(self):
        return self.rect.y

class badguy(Player):
    # Initialize the bad guy
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.images = []
        self.img = py.image.load(os.path.join('../Images/fixed-hitbox-moving-ghoul-toad.png')).convert_alpha()
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
    def tilex(self):
        return self.rect.x
    def tiley(self):
        return self.rect.y




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


active_height = [0]

class new_plat:
    active_class = None
    hchange = 0
    def __init__(self,offset,offset_y,size,pc,obs,mov,height,ah):
        self.offset = offset
        self.offset_y = offset_y
        self.size = size
        self.pc = pc
        self.obs = obs
        self.mov = mov
        self.height = height
        self.ah = ah


# Function to create a platform at a given offset
    def platform1(self):
        p1l = []
        self.platsg = py.sprite.Group()
        for i in range(self.size):
            p1l.append(tile_s * i + 900 + self.offset)

        for i in range(len(p1l)):
            self.platholder = tile(p1l[i], self.offset_y, 'Ground V1.png')
            self.pc.append(self.platholder.rect)
            self.platsg.add(self.platholder)

        return self.platsg


    def collisons(self):
        ac = abs(camera_offset_x)+100
        for i in self.obs:

            if player.rect.colliderect(i):
                new_plat.active_class = self
                new_plat.hchange = self.height
                self.ah[0] = self.height

                if (player.rect.y < self.height):
                    self.mov[2] = 734
                    break

                if ac < i.x:
                    self.mov[0] = 634
                    if jump[0]:
                        self.mov[2] = 734

                    break
                if ac >i.x:
                    if jump[0]:
                        self.mov[2] = 734
                    self.mov[1]=634
                    break

            else:
                 self.mov[0] = 1
                 self.mov[1] = 1
                 self.mov[2] = 1
                 new_plat.hchange = 0
                 self.ah[0] = 0
    def plat_return(self):
        return self.obs

def which_platform(plat_list,player,active_height):
    for i in range(len(plat_list)):
        for x in range(len(plat_list[i].plat_return())):
            if player.colliderect(plat_list[i].plat_return()[x]) :
                plat_list[i].collisons()
                break





player = Player()
player.rect.x = 500
player.rect.y = 450
player_list = py.sprite.Group()
player_list.add(player)

badguy1 = badguy()
badguy1x = 1000

badguy1.rect.x=badguy1x
bxcounter = 0

badguy1.rect.y = 469.5
badguy_list = py.sprite.Group()
badguy_list.add(badguy1)
active_player_height = 0
def draw_ground(x_location, y_location, x_size, y_size):
    image_block = py.image.load(os.path.join('ground V1.png')).convert_alpha()
    image_block = py.transform.scale(image_block, (32, 32))

    for i in range(x_size + 1):

        current_x_size = i * 32

        #win.blit(image_block, (x_location + current_x_size, y_location))

        for z in range(y_size + 1):

            current_y_size = z * 32

            win.blit(image_block, (x_location + current_x_size, y_location + current_y_size))






bxadd = 5

move = [1,1,1]

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
    badguy1.rect.x = badguy1x


    if not player_x_position >= 630 and key[py.K_d] or key[py.K_RIGHT] and player_x_position >= 630:
        player_x_position += vel
        if player_facing_right == False:
            player_facing_right = True
            player.update_image(player_facing_right)
    else:
        player_x_position == 630

    # --Key D--
    if player_x_position == 630 and (key[py.K_d] or key[py.K_RIGHT]) and player_x_position == 630 and move[0] == 1:

        if player_facing_right == False:
            player_facing_right = True
            player.update_image(player_facing_right)

        if key[py.K_d] and key[py.K_LSHIFT] or key[py.K_RIGHT] and key[py.K_LSHIFT]:
            camera_offset_x += -(run_vel)

        else:
            camera_offset_x += -(vel)

    # --Key A--
    if player_x_position == 615 and (key[py.K_a] or key[py.K_LEFT]) and player_x_position == 615 and move[1] ==1 :

        if player_facing_right == True:
            player_facing_right = False
            player.update_image(player_facing_right)

        if key[py.K_a] and key[py.K_LSHIFT] or key[py.K_LEFT] and key[py.K_LSHIFT]:
            camera_offset_x += run_vel

        else:
            camera_offset_x += vel

    elif (key[py.K_a] or key[py.K_LEFT]) and move[1] ==1 :

        if player_facing_right == True:
            player_facing_right = False
            player.update_image(player_facing_right)

        if key[py.K_a] and key[py.K_LSHIFT] or key[py.K_LEFT] and key[py.K_LSHIFT]:
            camera_offset_x += run_vel

        else:
            camera_offset_x += vel


    if move[2] ==1 and jump[0] == False:
        ground_height = 469.5
        if player_y_position < ground_height:
            player_y_position += 10
    if jump[0] == False:



        if move[2]==1 and (key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]) and player_y_position >=469.5:
            jump[0] = True





    # --Deals with the player jumping
    else:

        if jc >= -12:
            player_y_position -= (jc * abs(jc)) * (1 / 3)
            jc -= 1
            print('j1')

        elif player_y_position >468:  # This will execute if our jump is finished
                jc = 12
                jump[0] = False
        elif move[2] == 1 and jc == -13:
            player_y_position = 469.5




# moves bad guy by moving him each cycle and then switching direction back once a counter reaches a certain number

    badguy1x = camera_offset_x + bxcounter+300
    if bxcounter >= 500:
        bxadd = -5
    elif bxcounter < 0 :
        bxadd = 5
    bxcounter += bxadd
    print(bxcounter)

    print('this guys dead')
    # camera_offset_x = resolution_width // 2 - player_x_position - width // 2

    win.fill((173, 216, 230))  # Fills the screen with blue

    # player =  py.draw.rect(win, (76, 12, 200),  (player_x_position, player_y_position, width, length))  # This takes: window/surface, color, rect

    # py.draw.rect(win, (200, 76, 12), (0, 560, 10000, 800))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    # py.draw.rect(win, (200, 76, 12),
    # (camera_offset_x, 590, 10000, 500))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

    block((50 + camera_offset_x), 50, 100, 100, 0, 0, 0, player_x_position)  # THIS IS THE BLACK BOX

#draw player, bad guy
    player_list.draw(win)
    badguy_list.draw(win)


    py.draw.rect(win, (255, 255, 255), player.rect, 2) # shows players hitbox
     # shows players hitbox
    pch = []
    pch2 = []
    move = [1,1,1]
    #       L,   R, j
    #platform1(camera_offset_x,500,10,pch).draw(win)
    #collisons(pch,move)
    active_height = [0]

# set up objects of platform class, put them in a list that we iterate through to detect active platform to determine height
    draw_ground(0+camera_offset_x,560,200,5)
    test_plat = new_plat(camera_offset_x+400,475,35,pch,pch,move,400,active_height)
    test_plat.platform1().draw(win)
    test2 = new_plat(camera_offset_x + 1600, 375, 4, pch2, pch2, move, 300,  active_height)
    test2.platform1().draw(win)
    platform_list = [test_plat,test2]

    which_platform(platform_list,player.rect,active_height)

    #jumping from platform

    if move[2] != 1 and (key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]) :
        jump[0] = True
        # set player height to active platform height
    if move[2] != 1:
        player_y_position = active_height[0] - 8
        if jump[0] == True:
            if jc >= -12:
                player_y_position -= (jc * abs(jc)) * (1 / 3)
                jc -= 1
                print('sq')
                jc2 = jc


            else:  # This will execute if our jump is finished
                jc = 12
                jump[0] = False
                print('good')

# if player collides with bad guy head on, player dies, if he collides from the bad guys head bad guy dies
    if  player.rect.colliderect(badguy1.rect) and player.rect.y ==badguy1.rect.y and (badguy1 in badguy_list):
        py.QUIT('you died')
    if player.rect.colliderect(badguy1.rect) :
        print('kill confirmed')
        badguy_list.remove(badguy1)





   # py.draw.rect(win, (255, 255, 255), badguy1.rect, 2)

    cheight = active_height
    # update display
    py.display.update()
    # --Prints player coord's, currently commeted out, cause reduces frames
py.quit()