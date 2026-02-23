#Import necessary modules
import pygame as py
import os
import sys


#https://code-with-me.global.jetbrains.com/ZMbp8Rn85_2s0dowIs_doA#p=PC&fp=1E99570F43DC2D4ECEAAD5CF6A800A7A264CA58EE43E7A707405663FF1C95287
#Initialize py



def game():
    gameplay_music = py.mixer.Sound("Mario_Gameplay_Music.mp3")
    gameplay_music.play()





    global transition_done
    global transition_size
    global inverse_transition_size
    global transition_start



    transition_done = False
    transition_size = 0  # 16
    inverse_transition_size = 1100
    transition_start = False

    def transition():
        global transition_done
        global transition_size
        global inverse_transition_size

        if not transition_done:
            if transition_size == 1100:
                transition_done = True
                transition_size = 0
                inverse_transition_size = 0
            else:
                transition_size += 13.75
                inverse_transition_size -= 13.75

            return transition_done
        transition_circle = pygame.draw.circle(win, (0, 0, 0), (resolution_width // 2, resolution_height // 2),
                                               transition_size)
    class Transition:

        def __init__(self, transition_start, menu_quit_selection):
            self.transition_start = transition_start
            self.menu_quit_selection = menu_quit_selection
            self.transition_done = False

        def transition_play(self):
            global transition_done
            global transition_size

            if not transition_done:
                if round(transition_size, 2) == 1100:
                    self.transition_done = True
                    transition_size = 0
                else:
                    transition_size += 4.4

            transition_circle = py.draw.circle(win, (0, 0, 0), (resolution_width // 2, resolution_height // 2),
                                                   transition_size)

        def transition_reverse(self):
            global transition_done
            global inverse_transition_size

            if not transition_done:
                if round(inverse_transition_size, 2) == 0:
                    self.transition_done = True
                    inverse_transition_size = 1100
                else:
                    inverse_transition_size -= 4.4

            transition_circle = py.draw.circle(win, (0, 0, 0), (resolution_width // 2, resolution_height // 2),
                                                   inverse_transition_size)

    quit_menu_transition = Transition(False, 1)








    # Menu
    menu_play_image = py.image.load(os.path.join('../Images/Menu_Play.png')).convert_alpha()
    menu_play_image = py.transform.scale(menu_play_image, (1280, 720))

    menu_login_image = py.image.load(os.path.join('../Images/Menu_Login.png')).convert_alpha()
    menu_login_image = py.transform.scale(menu_login_image, (1280, 720))

    menu_stats_image = py.image.load(os.path.join('../Images/Menu_Stats.png')).convert_alpha()
    menu_stats_image = py.transform.scale(menu_stats_image, (1280, 720))

    menu_settings_image = py.image.load(os.path.join('../Images/Menu_Settings.png')).convert_alpha()
    menu_settings_image = py.transform.scale(menu_settings_image, (1280, 720))

    menu_quit_yes = py.image.load(os.path.join('../Images/Menu_Quit (YES).png')).convert_alpha()
    menu_quit_yes = py.transform.scale(menu_quit_yes, (1280, 720))

    menu_quit_no = py.image.load(os.path.join('../Images/Menu_Quit (NO).png')).convert_alpha()
    menu_quit_no = py.transform.scale(menu_quit_no, (1280, 720))

    button_select_sound = py.mixer.Sound("../Sounds/Mario_Selection_Sound.mp3")
    menu_music = py.mixer.Sound("../Sounds/Mario_Menu_Music.mp3")











    py.init()

    # Set the camera offset
    camera_offset_x = 0

    # Set the resolution of the game window
    resolution_width = 1280
    resolution_height = 720  # Running 720p currently
    win = py.display.set_mode((resolution_width, resolution_height))

    camera_offset_x = 0
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
    jump = [False]
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
    #grass_locations = []
    #grass_list = py.sprite.Group()
    tile_s = 32
    #for i in range(150):
        #grass_locations.append(tile_s * i)
    #for i in range(len(grass_locations)):
        #grass_holder = tile(grass_locations[i], 560, 'Ground V1.png')
        #for w in range(0, 160, 32):
            #dirt_holder = tile(grass_locations[i], 560 + w, 'Ground V1.png')
            #grass_list.add(dirt_holder)
        #grass_list.add(grass_holder)


    def draw_ground(x_location, y_location, x_size, y_size):
        image_block = py.image.load(os.path.join('../Images/Ground V1.png')).convert_alpha()
        image_block = py.transform.scale(image_block, (32, 32))

        for i in range(x_size + 1):

            current_x_size = i * 32

            #win.blit(image_block, (x_location + current_x_size, y_location))

            for z in range(y_size + 1):

                current_y_size = z * 32
                print(current_x_size)
                print(current_y_size, "y")
                win.blit(image_block, (x_location + current_x_size, y_location + current_y_size))



    # Function to create a platform at a given offset
    def platform1(offset,offset_y,size,pc):
        p1l = []
        platsg = py.sprite.Group()
        for i in range(size):
            p1l.append(tile_s * i + 900 + offset)

        for i in range(len(p1l)):
            platholder = tile(p1l[i], offset_y, 'Ground V1.png')
            pc.append(platholder.rect)
            platsg.add(platholder)

        return platsg


    player = Player()
    player.rect.x = 500
    player.rect.y = 450
    player_list = py.sprite.Group()
    player_list.add(player)


    def collisons(obs,mov):
        ac = abs(camera_offset_x)+100
        for i in obs:

            if player.rect.colliderect(i):
                print('collided')



                if (player.rect.y < 425):
                    mov[2] = 734
                    break

                if ac < i.x:
                    mov[0] = 634
                    if jump[0]:
                        mov[2] = 734

                    break
                if ac >i.x:
                    if jump[0]:
                        mov[2] = 734
                    mov[1]=634
                    break

            else:
                 mov[0] = 1
                 mov[1] = 1
                 mov[2] = 1






    move = [1,1,1]

    # --Runs player's movements--
    while active:
        py.time.delay(25)
        for event in py.event.get():
            if event.type == py.QUIT:
                active = False

        key = py.key.get_pressed()



        if key[py.K_ESCAPE]:
            # if not quit_menu_transition.transition_done:
            quit_menu_transition.transition_start = True

        elif quit_menu_transition.transition_done and quit_menu_transition.transition_start:
            win.fill((0, 0, 0))

            # CAUSE DRAWN IN HERE
            if (key[py.K_a] or key[py.K_LEFT]) and quit_menu_transition.menu_quit_selection > 1:
                quit_menu_transition.menu_quit_selection -= 1
                button_select_sound.play()
            elif (key[py.K_d] or key[py.K_RIGHT]) and quit_menu_transition.menu_quit_selection < 2:
                quit_menu_transition.menu_quit_selection += 1
                button_select_sound.play()

            print(quit_menu_transition.menu_quit_selection)

            if quit_menu_transition.menu_quit_selection == 1:
                win.blit(menu_quit_yes, (0, 0))

                if key[py.K_RETURN]:
                    done = True

            elif quit_menu_transition.menu_quit_selection == 2:
                win.blit(menu_quit_no, (0, 0))

                if key[py.K_RETURN]:
                    quit_menu_transition.transition_start = False
                    quit_menu_transition.transition_done = False
                    quit_menu_transition.menu_quit_selection = 1
                    # quit_menu_transition.transition_reverse(1100)

        if quit_menu_transition.transition_start:
            if not quit_menu_transition.transition_done:
                quit_menu_transition.transition_play()





        # print(1000 + camera_offset_x, "LESS")
        # print(1000 + 200 + camera_offset_x, "MORE")
        # print(player_x_position)
        # player.img = py.transform.flip(player.img, True, False)

            # --Gets what key the player has pressed--
        
        # else:
        # camera_offset_x = 0
        player.rect.x = player_x_position
        player.rect.y = player_y_position

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

            # --Key S-- (But first determines if player is mid-air/jumping)
            if (key[py.K_s] and player_y_position < ground_height ) or (
                    key[py.K_DOWN] and player_y_position < ground_height):

                if key[py.K_s] and key[py.K_LSHIFT] or key[py.K_DOWN] and key[py.K_LSHIFT]:
                    player_y_position += run_vel
                elif player_y_position < ground_height:
                    player_y_position += vel





            # --Key W-- (But first determines if player is mid-air/jumping)


            if move[2]==1 and (key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]) and player_y_position >=469.5:
                jump[0] = True




        # --Deals with the player jumping
        else:

            if jc >= -12:
                player_y_position -= (jc * abs(jc)) * (1 / 3)
                jc -= 1
            else:  # This will execute if our jump is finished
                jc = 12
                jump[0] = False









        # camera_offset_x = resolution_width // 2 - player_x_position - width // 2

        win.fill((173, 216, 230))  # Fills the win with blue

        # player =  py.draw.rect(win, (76, 12, 200),  (player_x_position, player_y_position, width, length))  # This takes: window/surface, color, rect

        # py.draw.rect(win, (200, 76, 12), (0, 560, 10000, 800))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

        # py.draw.rect(win, (200, 76, 12),
        # (camera_offset_x, 590, 10000, 500))  # This takes: window/surface, color, rect, (THIS IS THE FLOOR)

        block((50 + camera_offset_x), 50, 100, 100, 0, 0, 0, player_x_position)  # THIS IS THE BLACK BOX


        player_list.draw(win)


        #grass_list.draw(win)
        py.draw.rect(win, (255, 255, 255), player.rect, 2) # shows players hitbox
         # shows players hitbox
        pch = []
        move = [1,1,1]
        #       L,   R, j
        platform1(camera_offset_x,500,10,pch).draw(win)


        collisons(pch,move)

        if move[2] != 1 and (key[py.K_w] or key[py.K_UP] or key[py.K_SPACE]) :
            jump[0] = True
        if move[2] != 1:
            player_y_position = 411

            if jump[0] == True:
                if jc >= -12:
                    player_y_position -= (jc * abs(jc)) * (1 / 3)
                    jc -= 1
                else:  # This will execute if our jump is finished
                    jc = 12
                    jump[0] = False

        draw_ground(0 + camera_offset_x, 560, 30, 5)
        py.draw.rect(win, (255, 255, 255), pch[0], 2)
        print( player_y_position)
        py.display.update()
        # --Prints player cord's, currently commeted out, cause reduces frames
       # print(player_x_position, ',', player_y_position)

if __name__ == "__game__":
    game()